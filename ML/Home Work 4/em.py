"""Mixture model for matrix completion"""
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture

def pdf_Normal(x, mu, sigma2,d=1):
    '''
    :returns the pdf of N(mu, sigma^2) at the point x
    :param x: (d,) numpy array
    :param mu:(d,) numpy array 
    :param sigma2: float
    :return: float
    '''
    return np.exp((np.linalg.norm(x-mu))**2/(-2*sigma2))/(2*np.pi*sigma2)**(d/2)

def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment

    """
    n, d = X.shape
    p_x_i=np.zeros((n, len(mixture.p)), dtype=float)
    for k,x_i in enumerate(X):
        for i,pi in enumerate(mixture.p):
            Cu= [j for j,x in enumerate(x_i) if x!=0]
            xu=np.array([x for x in x_i if x != 0],dtype=float) 
            mu= np.array([mixture.mu[i][j] for j in Cu],dtype=float)
            var = mixture.var[i]
            d=len(Cu)
            p_x_i[k][i]= pi*pdf_Normal(xu,mu,var,d)    
    p_x_i+=1e-16
    p_x_i_sum = np.sum(p_x_i,axis=1) 
    p_j_u = p_x_i/ p_x_i_sum[:, None]   
    loglike = np.sum(np.log(p_x_i_sum))
    return p_j_u , loglike



def mstep(X: np.ndarray, post: np.ndarray, mixture: GaussianMixture,
          min_variance: float = .25) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        post: (n, K) array holding the soft counts
            for all components for all examples
        mixture: the current gaussian mixture
        min_variance: the minimum variance for each gaussian

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    _, K = post.shape
    p_sum = np.sum(post,axis=0)
    p= p_sum/n       
    mu = mixture.mu
    var = mixture.var
    CuT = X >0
    denominator= np.sum(post,axis=1) @ np.sum(CuT,axis=1)
    for j in range(K):  
        for i in range(d):
            mu[j, i] = np.sum(post[:,j]*X[:,i]) / np.sum(post[:,j]*CuT[:,i])       
        normMat = ((mu[j] - X)**2) * CuT
        sse = normMat.sum(axis=1) @ post[:, j]
        
        
        var[j] = sse / denominator
        if var[j]<.25:
            var[j]=.25
    return GaussianMixture(mu, var, p)


def run(X: np.ndarray, mixture: GaussianMixture,
        post: np.ndarray) -> Tuple[GaussianMixture, np.ndarray, float]:
    """Runs the mixture model

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the current assignment
    """
    prev_cost = None
    cost = None
    while (prev_cost is None or abs(prev_cost - cost) > 1e-6*abs(cost)):
        prev_cost = cost
        post, cost= estep(X, mixture)
        mixture = mstep(X,post, mixture)

    return mixture, post, cost


def fill_matrix(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fills an incomplete matrix according to a mixture model

    Args:
        X: (n, d) array of incomplete data (incomplete entries =0)
        mixture: a mixture of gaussians

    Returns
        np.ndarray: a (n, d) array with completed data
    """
    n, d = X.shape
    p_x_i=np.zeros((n, len(mixture.p)), dtype=float)
    for k,x_i in enumerate(X):
        for i,pi in enumerate(mixture.p):
            Cu= [j for j,x in enumerate(x_i) if x!=0]
            xu=np.array([x for x in x_i if x != 0],dtype=float) 
            mu= np.array([mixture.mu[i][j] for j in Cu],dtype=float)
            var = mixture.var[i]
            d=len(Cu)
            p_x_i[k][i]= pi*pdf_Normal(xu,mu,var,d)    
    p_x_i+=1e-16
    p_x_i_sum = np.sum(p_x_i,axis=1) 
    p_j_u = p_x_i/ p_x_i_sum[:, None] 


    K = len(mixture.p)
    return_X = np.copy(X)
    p, mu,var = mixture.p,mixture.mu,mixture.var
    probmu= p_j_u @ mu
    print(probmu)
    for i in range(n):
        for j in range(d):
            if X[i,j]==0:
                return_X[i,j]=probmu[i,j]
    return return_X
