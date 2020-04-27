"""Mixture model using EM"""
from typing import Tuple
import numpy as np
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
        X: (n, d) array holding the data
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment
    """
    
    p_x_i=np.array([[pi*pdf_Normal(x_i,mixture.mu[i],mixture.var[i],d=len(x_i))  for i, pi in enumerate(mixture.p)] for x_i in X],dtype=float)
    p_x_i_sum = np.sum(p_x_i,axis=1) 
    
    p_j_i = p_x_i/ p_x_i_sum[:, None]   
    
    
    loglike = np.sum(np.log(p_x_i_sum))

    return p_j_i , loglike


def mstep(X: np.ndarray, post: np.ndarray) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    _, K = post.shape

    p_sum = np.sum(post,axis=0)
    p= p_sum/n
    
    
    mu = np.zeros((K, d),dtype=float)
    var = np.zeros(K,dtype=float)

    for j in range(K):
        mu[j, :] = post[:, j] @ X / p_sum[j]
        sse = ((mu[j] - X)**2).sum(axis=1) @ post[:, j]
        var[j] = sse / (d * p_sum[j])


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
        mixture = mstep(X, post)

    return mixture, post, cost
