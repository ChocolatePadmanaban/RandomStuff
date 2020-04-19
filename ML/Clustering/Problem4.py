#EM Algorithm

import numpy as np 
import scipy.stats 

def pdf_Normal(x, mu, sigma2):
    '''
    :returns the pdf of N(mu, sigma^2) at the point x
    :param x: (d,) numpy array
    :param mu:(d,) numpy array 
    :param sigma2: float
    :return: float
    '''
    return scipy.stats.norm(mu,sigma2**.5).pdf(x)


def log_likelihood(x_list, pi_list, mu_list, sigma2_list):
    prob_list = np.array([np.sum([pi_list[i]*pdf_Normal(x,mu_list[i],sigma2_list[i]) for i in range(len(pi_list))]) for x in x_list],dtype='float')
    log_list= np.log(prob_list)
    return np.sum(log_list)


def P_x_i(x_i,p_list,mu_list,sigma_list):
    return sum([p_list[i]*pdf_Normal(x_i,mu_list[i],sigma_list[i])  for i in range(len(p_list))])

def P_j_i(x_i,p_list, mu_list, sigma_list,j):
    p_x_i= P_x_i(x_i,p_list,mu_list,sigma_list)
    p_j_i= p_list[j]*pdf_Normal(x_i,mu_list[j],sigma_list[j])/ p_x_i
    return p_j_i



def Check_Prob(x,p_list,mu_list,sigma_list):
    TotalProb= sum([sum([ P_j_i(x[i],p_list,mu_list,sigma_list,j)  for i in range(len(x))]) for j in range(len(p_list))   ])
    print(TotalProb)
    if len(x)==TotalProb:
        return True
    return False

def M_step(p_j_i_list, x):
    sumpji= sum(p_j_i_list)
    p_j = sumpji/len(x)
    mu_j = sum([p_j_i_list[i]*x[i]  for i in range(len(x))])/sumpji
    sigma2_j= sum([p_j_i_list[i]*(x[i]-mu_j)**2  for i in range(len(x))])/sumpji
    return p_j, mu_j, sigma2_j

def EM_oneIterate(x_list,pi_list,mu_list,sigma2_list):
    p= [[P_j_i(x_list[i],pi_list,mu_list,sigma2_list,j) for i in range(len(x_list))]  for j in range(len(pi_list))]
    return [M_step(i,x_list) for i in p] 

def EM(x_list,pi_list,mu_list,sigma2_list):
    for _ in range(30):
        temp = EM_oneIterate(x_list,pi_list,mu_list,sigma2_list)
        pi_list,mu_list,sigma2_list=[],[],[]
        for i in range(len(temp)):
            pi_list.append(temp[i][0])
            mu_list.append(temp[i][1])
            sigma2_list.append(temp[i][2])
        pi_list,mu_list,sigma2_list= np.array(pi_list,dtype='float'),np.array(mu_list,dtype='float'),np.array(sigma2_list,dtype='float')
    return  pi_list,mu_list,sigma2_list


if __name__ == "__main__":
    x_list= np.array([-1,0,4,5,6],dtype='float')
    pi_list= np.array([.5,.5])
    mu_list= np.array([6.,7])
    sigma2_list = np.array([1.,4]) 
    print("log likelihood is :  ", log_likelihood(x_list,pi_list,mu_list,sigma2_list))
    print(np.array([[pi_list[i]*pdf_Normal(x,mu_list[i],sigma2_list[i]) for i in range(len(pi_list))] for x in x_list],dtype='float'))

    print(EM(x_list,pi_list,mu_list,sigma2_list))

    # p_j_i_list = [P_j_i(x_list[i],pi_list,mu_list,sigma2_list,1) for i in range(len(x_list))]
    # print("Is Probability Checked:  " , Check_Prob(x_list,pi_list,mu_list,sigma2_list))
    # print(" the Parameters of M_step is",M_step(p_j_i_list, x_list) )
