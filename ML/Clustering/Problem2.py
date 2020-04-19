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



if __name__ == "__main__":
    x= np.array([.2,-.9,-1,1.2,1.8])
    p_list= [.5,.5]
    mu_list=[-3,2]
    sigma_list=[4,4]
    for i in range(len(x)):
        print("P(j|i):  " , P_j_i(x[i],p_list,mu_list,sigma_list,0))
    p_j_i_list = [P_j_i(x[i],p_list,mu_list,sigma_list,0) for i in range(len(x))]
    print("Is Probability Checked:  " , Check_Prob(x,p_list,mu_list,sigma_list))
    print(" the Parameters of M_step is",M_step(p_j_i_list, x) )
