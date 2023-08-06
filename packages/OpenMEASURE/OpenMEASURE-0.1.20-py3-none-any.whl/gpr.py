'''
MODULE: gpr.py
@Authors:
    A. Procacci [1]
    [1]: Université Libre de Bruxelles, Aero-Thermo-Mechanics Laboratory, Bruxelles, Belgium
@Contacts:
    alberto.procacci@ulb.be
@Additional notes:
    This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
    Please report any bug to: alberto.procacci@ulb.be
'''

import copy
import numpy as np
import torch
import gpytorch
from scipy.stats import kurtosis
from gpytorch.likelihoods import MultitaskGaussianLikelihood
from gpytorch.means import ConstantMean
from gpytorch.kernels import ScaleKernel, MaternKernel
from gpytorch.distributions import MultitaskMultivariateNormal, MultivariateNormal
from gpytorch.mlls import ExactMarginalLogLikelihood
import sparse_sensing as sps

class ExactGPModel(gpytorch.models.ExactGP):
    '''
    Subclass used to build an exact GP Model inheriting from the ExactGP model.
    
    Attributes
    ----------
    X_train : numpy array
        matrix of dimensions (p,d) where p is the number of operating conditions
        and d is the number of design features.
    
    Y_train : numpy array
        matrix of dimensions (p,q) where p is the number of operating conditions
        and q is the number of retained coefficients.

    likelihood : gpytorch.likelihoods
        one dimensional likelihood from gpytorch.likelihoods.
        
    mean : gpytorch.means
        mean function gpytorch.means.
    
    kernel : gpytorch.kernels
        kernel function from gpytorch.kernels.
        
    Methods
    ----------
    forward(x)
        Return the multivariate distribution given the input x.
    
    '''
    
    def __init__(self, X_train, Y_train, likelihood, mean, kernel):
        super().__init__(X_train, Y_train, likelihood)
        
        self.mean_module = mean
        self.covar_module = ScaleKernel(kernel)
            
    def forward(self, x):
        mean_x = self.mean_module(x)
        kernel_x = self.covar_module(x)
        return MultivariateNormal(mean_x, kernel_x)

class BatchIndipendentMultitaskGPModel(gpytorch.models.ExactGP):
    '''
    Subclass used to build a Multitask GP Model inheriting from the ExactGP model. 
    A Multitask model is needed when the target variable has multiple components.
    
    Attributes
    ----------
    X_train : numpy array
        matrix of dimensions (p,d) where p is the number of operating conditions
        and d is the number of design features.
    
    Y_train : numpy array
        matrix of dimensions (p,q) where p is the number of operating conditions
        and q is the number of retained coefficients.
        
    likelihood : gpytorch.likelihoods.MultitaskGaussianLikelihood
        multi-dimensional likelihood from gpytorch.likelihoods.MultitaskGaussianLikelihood.
        
    mean : gpytorch.means
        mean function gpytorch.means.
    
    kernel : gpytorch.kernels
        kernel function from gpytorch.kernels.    
        
    Methods
    ----------
    forward(x)
        Return the multivariate distribution given the input x.
    
    '''
    
    def __init__(self, X_train, Y_train, likelihood, mean, kernel):
        super().__init__(X_train, Y_train, likelihood)
        
        self.n_tasks = Y_train.shape[1]
        shape = torch.Size([self.n_tasks])
        
        if len(mean.batch_shape) > 0:
            self.mean_module = mean
        else:
            self.mean_module = ConstantMean(batch_shape=shape)
        
        if len(kernel.batch_shape) > 0:
            self.covar_module = ScaleKernel(kernel, batch_shape=shape)
        else:
            self.covar_module = ScaleKernel(MaternKernel(batch_shape=shape), 
                                                         batch_shape=shape)
        
    def forward(self, x):
        mean_x = self.mean_module(x)
        kernel_x = self.covar_module(x)
        return MultitaskMultivariateNormal.from_batch_mvn(MultivariateNormal(mean_x, 
                                                                             kernel_x))
    
class GPR(sps.ROM):
    '''
    Class used for building a GPR-based ROM.
    
    Attributes
    ----------
    X : numpy array
        data matrix of dimensions (n,p) where n = n_features * n_points and p
        is the number of operating conditions.
        
    n_features : int
        the number of features in the dataset (temperature, velocity, etc.).
    
    xyz : numpy array
        3D position of the data in X, size (nx3).
    
    P : numpy array
        Design features matrix of dimensions (p,d) where p is the number of 
        operating conditions.
    
    gpr_type : str, optional.
        If 'SingleTask', a GPR model is trained for each of the r latent dimensions.
        If 'MultiTask', the a single multitask GPR is trained for all the latent dimensions.
        The default is 'SingleTask'. 
    
    likelihood : gpytorch.likelihoods, optional
        The likelihood passed to the GPR model. If gpr_type='SingleTask', the default 
        is GaussianLikelihood(). If gpr_type='MultiTask', the MultitaskGaussianLikelihood()
        is the only option.

    mean : gpytorch.means, optional.
        The mean passed to the GPR model. The default is means.ConstantMean.

    kernel : gpytorch.kernels, optional.
        The kernel used for the computation of the covariance matrix. The default
        is the Matern kernel.
        
        
    Methods
    ----------
    scale_coefficients(A, scale_type)
        Scales the coefficients used for training the GPR model.
        
    unscale_coefficients(scale_type)
        Unscale the coefficients.
    
    fit_predict(xs, scale_type='std', select_modes='variance', 
                n_modes=99)
        Trains the GPR model, then predicts ar and reconstructs x.
    
    predict(xs, scale_type='std'):
        Predicts ar and reconstructs x.
    
    '''

    def __init__(self, X, n_features, xyz, P, gpr_type='SingleTask', likelihood=None, 
                 kernel=None, mean=None):
        super().__init__(X, n_features, xyz)
        self.P = P
        self.gpr_type = gpr_type
        
        if likelihood is None:
            self.likelihood = gpytorch.likelihoods.GaussianLikelihood()
        else:
            self.likelihood = likelihood
        if kernel is None:
            self.kernel = gpytorch.kernels.MaternKernel(2.5)
        else:
            self.kernel = kernel
        if mean is None:
            self.mean = gpytorch.means.ConstantMean()
        else:
            self.mean = mean

    def scale_GPR_data(self, P, scale_type):
        '''
        Return the scaled input and target for the GPR model.

        Parameters
        ----------
        P : numpy array
            Data matrix to scale, size (p,d). 
        
        scale_type : str
            Type of scaling.

        Returns
        -------
        P0: numpy array
            The scaled measurement vector.

        '''
        
        P_cnt = np.zeros_like(P)
        P_scl = np.zeros_like(P)
        
        for i in range(P.shape[1]):
            x = P[:,i]
            P_cnt[:,i] = np.mean(x)
            
            if scale_type == 'std':
                P_scl[:,i] = np.std(x)
            
            elif scale_type == 'none':
                P_scl[:,i] = 1.
            
            elif scale_type == 'pareto':
                P_scl[:,i] = np.sqrt(np.std(x))
            
            elif scale_type == 'vast':
                scl_factor = np.std(x)**2/np.average(x)
                P_scl[:,i] = scl_factor
            
            elif scale_type == 'range':
                scl_factor = np.max(x) - np.min(x)
                P_scl[:,i] = scl_factor
                
            elif scale_type == 'level':
                P_scl[:,i] = np.average(x)
                
            elif scale_type == 'max':
                P_scl[:,i] = np.max(x)
            
            elif scale_type == 'variance':
                P_scl[:,i] = np.var(x)
            
            elif scale_type == 'median':
                P_scl[:,i] = np.median(x)
            
            elif scale_type == 'poisson':
                scl_factor = np.sqrt(np.average(x))
                P_scl[:,i] = scl_factor
            
            elif scale_type == 'vast_2':
                scl_factor = (np.std(x)**2 * kurtosis(x, None)**2)/np.average(x)
                P_scl[:,i] = scl_factor
            
            elif scale_type == 'vast_3':
                scl_factor = (np.std(x)**2 * kurtosis(x, None)**2)/np.max(x)
                P_scl[:,i] = scl_factor
            
            elif scale_type == 'vast_4':
                scl_factor = (np.std(x)**2 * kurtosis(x, None)**2)/(np.max(x)-np.min(x))
                P_scl[:,i] = scl_factor
            
            elif scale_type == 'l2-norm':
                scl_factor = np.linalg.norm(x.flatten())
                P_scl[:,i] = scl_factor
            
            else:
                raise NotImplementedError('The scaling method selected has not been '\
                                          'implemented yet')
                    
        self.P_cnt = P_cnt
        self.P_scl = P_scl
        P0 = (P - P_cnt)/P_scl
        return P0    

    def fit(self, scaleX_type='std', scaleP_type='std', select_modes='variance', decomp_type='POD', 
            n_modes=99, max_iter=1000, rel_error=1e-5, lr=0.1, solver='ECOS', abstol=1e-3, verbose=False, 
            save_path=None):
        '''
        Fit the GPR model.
        Return the prediction vector.

        Parameters
        ----------
        xs : numpy array
            The set of design features to evaluate the prediction, size (n_p,d).
            
        scaleX_type : str, optional
            Type of scaling method for the data matrix. The default is 'std'.
        
        scaleP_type : str, optional
            Type of scaling method for the parameters. The default is 'std'.
        
        select_modes : str, optional
            Type of mode selection. The default is 'variance'. The available 
            options are 'variance' or 'number'.
            
        n_modes : int or float, optional
            Parameters that control the amount of modes retained. The default is 
            99, which represents 99% of the variance. If select_modes='number',
            n_modes represents the number of modes retained.
        
        max_iter : int, optional
            Maximum number of iterations to train the hyperparameters. The default
            is 1000.
            
        rel_error : float, optional
            Minimum relative error below which the training of hyperparameters is
            stopped. The default is 1e-5.
        
        lr : float, optional
            Learning rate of the Adam optimizer used for minimizing the negative log 
            likelihood. The default is 0.1.

        solver : str, optional
            Type of solver to use for solving the constrained minimization problem.
            Refer to the cvxpy documentation. The default is 'ECOS'.

        abstol : float, optional
            Absolute accuracy for the constrained solver used for CPOD. 
            Default is 1e-3.

        verbose : bool, optional
            If True, it will print informations on the training of the hyperparameters.
            The default is False.
            
        save_path : str, optional.
            String containing the path where to save the model (extension .pth).
            The default is None, and the model is not saved.

        Returns
        -------
        A_pred : numpy array
            The low-dimensional projection of the state of the system, size (n_p,q)
            
        Sigma_dev : numpy array
            Uncertainty in the prediction, size (n_p,q)
        
        '''
        
        self.scaleX_type = scaleX_type
        self.scaleP_type = scaleP_type
        
        X0 = self.scale_data(scaleX_type)
        
        Ur, Ar, exp_variance_r = self.decomposition(X0, decomp_type, select_modes, n_modes, solver, abstol, verbose)
        
        self.Ur = Ur
        self.Ar = Ar
        self.r = Ar.shape[1]
        self.d = self.P.shape[1]
        
        # Get the singular values and the orthonormal basis
        Vr = np.zeros_like(Ar)
        Sigma_r = np.zeros((self.r,))
        for i in range(self.r):
            Sigma_r[i] = np.linalg.norm(Ar[:,i])
            Vr[:,i] = Ar[:,i]/Sigma_r[i]
        
        self.Sigma_r = Sigma_r
        P0 = GPR.scale_GPR_data(self, self.P, scaleP_type)
        
        P0_torch = torch.from_numpy(P0).contiguous().float()
        Vr_torch = torch.from_numpy(Vr).contiguous().float()
        
        if self.gpr_type == 'MultiTask':
            models = []
            likelihoods = []
            likelihoods.append(MultitaskGaussianLikelihood(num_tasks=self.r))
            models.append(BatchIndipendentMultitaskGPModel(P0_torch, Vr_torch, likelihoods[0], 
                                                           self.mean, self.kernel))
        
            # Find optimal model hyperparameters
            models[0].train()
            likelihoods[0].train()
            
            # Use the adam optimizer
            # Includes GaussianLikelihood parameters
            optimizer = torch.optim.Adam(models[0].parameters(), lr=0.1)

            # "Loss" for GPs - the marginal log likelihood
            mll = ExactMarginalLogLikelihood(likelihoods[0], models[0])
            loss_old = 1e10
            e = 1e10
            i = 0
            while (e > rel_error) and (i < max_iter):
                optimizer.zero_grad()
                output = models[0](P0_torch)
                loss = -mll(output, Vr_torch)
                loss.backward()
                e = torch.abs(loss - loss_old).item()
                loss_old = loss
                if verbose == True:
                    print(f'Iter {i+1:d}/{max_iter:d} - Loss: {loss.item():.2e} - ' \
                         f'Noise: {models[0].likelihood.noise.item():.2e}')

                optimizer.step()
                i += 1

            if save_path is not None:
                torch.save(model.state_dict(), save_path)
            
            self.models = models
            self.likelihoods = likelihoods
        
        else:
            models = []
            likelihoods = []
            for i in range(self.r):
                likelihood = copy.deepcopy(self.likelihood)
                mean = copy.deepcopy(self.mean)
                kernel = copy.deepcopy(self.kernel)
                model = ExactGPModel(P0_torch, Vr_torch[:,i], likelihood, mean, kernel)
                
                model.train()
                likelihood.train()
            
                # Use the adam optimizer
                # Includes GaussianLikelihood parameters
                optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

                # "Loss" for GPs - the marginal log likelihood
                mll = ExactMarginalLogLikelihood(likelihood, model)
                loss_old = 1e10
                e = 1e10
                j = 0
                while (e > rel_error) and (j < max_iter):
                    optimizer.zero_grad()
                    output = model(P0_torch)
                    loss = -mll(output, Vr_torch[:,i])
                    loss.backward()
                    e = torch.abs(loss - loss_old).item()
                    loss_old = loss
                    if verbose == True:
                        noise_avg = np.mean(model.likelihood.noise.detach().numpy())
                        print(f'Iter {j+1:d}/{max_iter:d} - Mode: {i+1:d}/{self.r:d} - Loss: {loss.item():.2e} - ' \
                        f'Mean noise: {noise_avg:.2e}')

                    optimizer.step()
                    j += 1

                models.append(model)
                likelihoods.append(likelihood)

            self.models = models
            self.likelihoods = likelihoods
        
        return models, likelihoods
    
    def predict(self, xs):
        '''
        Return the prediction vector. 
        This method has to be used after fit_predict.

        Parameters
        ----------
        xs : numpy array
            The set of design features to evaluate the prediction, size (n_p,d).

        Returns
        -------
        A_pred : numpy array
            The low-dimensional projection of the state of the system, size (n_p,r)
        
        Sigma_dev : numpy array
            Uncertainty in the prediction, size (n_p,r)

        '''
        
        if hasattr(self, 'models'):
            if xs.ndim < 2:
                xs = xs[np.newaxis, :]

            n_p = xs.shape[0]

            xs0 = np.zeros_like(xs)
            for i in range(xs.shape[1]):
                xs0[:,i] = (xs[:,i] - self.P_cnt[0,i]) / self.P_scl[0,i]
            
            xs0_torch = torch.from_numpy(xs0).contiguous().float()
            
            if self.gpr_type == 'MultiTask':
            
                # Set into eval mode
                self.models[0].eval()
                self.likelihoods[0].eval()

                observed_pred = self.models[0](xs0_torch)
                V_pred = observed_pred.mean.detach().numpy()
                
                V_cov = observed_pred.lazy_covariance_matrix # covariance matrix
                V_sigma = np.sqrt(V_cov.diag().detach().numpy()) # standard deviation of prediction
                V_sigma = V_sigma.reshape((n_p, self.r))

            else:
                V_pred = np.zeros((n_p, self.r))
                V_sigma = np.zeros((n_p, self.r))

                for i in range(self.r):
                    # Set into eval mode
                    self.models[i].eval()
                    self.likelihoods[i].eval()

                    observed_pred = self.models[i](xs0_torch)
                    V_pred[:,i] = observed_pred.mean.detach().numpy()
                    
                    V_cov = observed_pred.lazy_covariance_matrix # covariance matrix
                    V_sigma[:,i] = np.sqrt(V_cov.diag().detach().numpy()) # standard deviation of prediction
        else:
            raise AttributeError('The function fit_predict has to be called '\
                                  'before calling predict.')
        A_pred = self.Sigma_r * V_pred
        A_sigma = self.Sigma_r * V_sigma
        return A_pred, A_sigma

    def reconstruct(self, Ar):
        '''
        Reconstruct the X matrix from the low-dimensional representation.

        Parameters
        ----------
        Ar : numpy array
            The matrix containing the low-dimensional coefficients, size (n_p,r).

        Returns
        -------
        X_rec : numpy array
            The high-dimensional representation of the state of the system, size (n,n_p)
            
        '''
        
        n_p = Ar.shape[0]
        n = self.Ur.shape[0]
        X_rec = np.zeros((n, n_p))
        for i in range(n_p):
            x0_rec = self.Ur @ Ar[i,:]
            X_rec[:,i] = self.unscale_data(x0_rec)

        return X_rec
    
if __name__ == '__main__':
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.tri as tri


    # Replace this with the path where you saved the data directory
    path = '../data/ROM/'

    # This is a n x m matrix where n = 165258 is the number of cells times the number of features
    # and m = 41 is the number of simulations.
    X_train = np.load(path + 'X_2D_train.npy')

    # This is a n x 4 matrix containing the 4 testing simulations
    X_test = np.load(path + 'X_2D_test.npy')

    features = ['T', 'CH4', 'O2', 'CO2', 'H2O', 'H2', 'OH', 'CO', 'NOx']
    n_features = len(features)

    # This is the file containing the x,z positions of the cells
    xz = np.load(path + 'xz.npy')
    n_cells = xz.shape[0]
    
    # Create the x,y,z array
    xyz = np.zeros((n_cells, 3))
    xyz[:,0] = xz[:,0]
    xyz[:,2] = xz[:,1]

    # This reads the files containing the parameters (D, H2, phi) with which 
    # the simulation were computed
    P_train = np.genfromtxt(path + 'parameters_train.csv', delimiter=',', skip_header=1)
    P_test = np.genfromtxt(path + 'parameters_test.csv', delimiter=',', skip_header=1)

    # Load the outline the mesh (for plotting)
    mesh_outline = np.genfromtxt(path + 'mesh_outline.csv', delimiter=',', skip_header=1)

    #---------------------------------Plotting utilities--------------------------------------------------
    def sample_cmap(x):
        return plt.cm.jet((np.clip(x,0,1)))

    def plot_sensors(xz_sensors, features, mesh_outline):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.plot(mesh_outline[:,0], mesh_outline[:,1], c='k', lw=0.5, zorder=1)
        
        features_unique = np.unique(xz_sensors[:,2])
        colors = np.zeros((features_unique.size,4))
        for i in range(colors.shape[0]):
            colors[i,:] = sample_cmap(features_unique[i]/len(features))
            
        for i, f in enumerate(features_unique):
            mask = xz_sensors[:,2] == f
            ax.scatter(xz_sensors[:,0][mask], xz_sensors[:,1][mask], color=colors[i,:], 
                       marker='x', s=15, lw=0.5, label=features[int(f)], zorder=2)

        
        ax.set_xlabel('$x (\mathrm{m})$', fontsize=8)
        ax.set_ylabel('$z (\mathrm{m})$', fontsize=8)
        eps = 1e-2
        ax.set_xlim(-eps, 0.35)
        ax.set_ylim(-0.15,0.7+eps)
        ax.set_aspect('equal')
        ax.legend(fontsize=8, frameon=False, loc='center right')
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top')
        wid = 0.3
        ax.xaxis.set_tick_params(width=wid)
        ax.yaxis.set_tick_params(width=wid)
        ax.set_xticks([0., 0.18, 0.35])
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        plt.show()

    def plot_contours_tri(x, y, zs, cbar_label=''):
        triang = tri.Triangulation(x, y)
        triang_mirror = tri.Triangulation(-x, y)

        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(6,6))
        
        z_min = np.min(zs)
        z_max = np.max(zs)
       
        n_levels = 12
        levels = np.linspace(z_min, z_max, n_levels)
        cmap_name = 'inferno'
        titles=['Original CFD','Predicted']
        
        for i, ax in enumerate(axs):
            if i == 0:
                ax.tricontourf(triang_mirror, zs[i], levels, vmin=z_min, vmax=z_max, cmap=cmap_name)
            else:
                ax.tricontourf(triang, zs[i], levels, vmin=z_min, vmax=z_max, cmap=cmap_name)
                ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False) 
            
            ax.set_aspect('equal')
            ax.set_title(titles[i])
            ax.set_xlabel('$x (\mathrm{m})$')
            if i == 0:
                ax.set_ylabel('$z (\mathrm{m})$')
        
        fig.subplots_adjust(bottom=0., top=1., left=0., right=0.85, wspace=0.02, hspace=0.02)
        start = axs[1].get_position().bounds[1]
        height = axs[1].get_position().bounds[3]
        
        cb_ax = fig.add_axes([0.9, start, 0.05, height])
        cmap = mpl.cm.get_cmap(cmap_name)
        norm = mpl.colors.Normalize(vmin=z_min, vmax=z_max)
        
        fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cb_ax, 
                    orientation='vertical', label=cbar_label)
        
        plt.show()
    #------------------------------------GPR ROM--------------------------------------------------
    # Create the gpr object
    noise = torch.from_numpy(1e-3*np.ones(P_train.shape[0])).float()
    likelihood = gpytorch.likelihoods.FixedNoiseGaussianLikelihood(noise=noise)
    n_modes = 10
    # likelihood = gpytorch.likelihoods.GaussianLikelihood()
    kernel = gpytorch.kernels.MaternKernel(ard_dims=n_modes)
    mean = gpytorch.means.ZeroMean()
    gpr = GPR(X_train, n_features, xyz, P_train, gpr_type='MultiTask', likelihood=likelihood,
              mean=mean, kernel=kernel)
    # gpr = GPR(X_train, n_features, xyz, P_train, gpr_type='SingleTask')
    
    # kernel = gpytorch.kernels.MaternKernel(ard_dims=n_modes, batch_shape=torch.Size([n_modes]))
    # mean = gpytorch.means.ZeroMean(batch_shape=torch.Size([n_modes]))
    # gpr = GPR(X_train, n_features, xyz, P_train, gpr_type='MultiTask',
    #           mean=mean, kernel=kernel)
    
    # gpr = GPR(X_train, n_features, xyz, P_train, gpr_type='MultiTask')

    # Calculates the POD coefficients ap and the uncertainty for the test simulations
    gpr.fit(verbose=False, rel_error=1e-3)
    Ap, Sigmap = gpr.predict(P_test)
    print(Sigmap)
    # Ap, Sigmap = gpr.fit_predict(P_test, decomp_type='POD', likelihood=likelihood, verbose=True)
    # Ap, Sigmap = gpr.fit_predict(P_test, decomp_type='POD', verbose=True)
    
    # Reconstruct the high-dimensional state from the POD coefficients
    Xp = gpr.reconstruct(Ap)

    # Select the feature to plot
    str_ind = 'OH'
    ind = features.index(str_ind)

    x_test = X_test[ind*n_cells:(ind+1)*n_cells,3]
    xp_test = Xp[ind*n_cells:(ind+1)*n_cells, 3]

    plot_contours_tri(xz[:,0], xz[:,1], [x_test, xp_test], cbar_label=str_ind)

