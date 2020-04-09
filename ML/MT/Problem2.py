import numpy as np 
import random


def get_order(n_samples):
    try:
        with open(str(n_samples) + '.txt') as fp:
            line = fp.readline()
            return list(map(int, line.split(',')))
    except FileNotFoundError:
        random.seed(1)
        indices = list(range(n_samples))
        random.shuffle(indices)
        return indices


def phiConversion(x):
    return np.array([[i[0]**2,i[0]*i[1]*2**.5,i[1]**2]  for i in x])


def LinearPerceptronAlgo(x,y):
    theta,theta_0 = np.zeros([1,3]),0
    alpha= []
    for _ in range(100):
        for i in get_order(x.shape[0]):
            alpha_0= 0
            
            if y[i]*(np.dot(theta, x[i])[0]+ theta_0) <= 0:
                theta += y[i]*x[i]
                theta_0 += y[i]
                alpha_0+=1
            alpha.append(alpha_0)
    return theta, theta_0, alpha


def calculatePerceptron(x,y,alpha):
    theta,theta_0 = np.zeros([1,3]),0
    for i in range(x.shape[0]):
        theta += alpha[i]*y[i]*x[i]
        theta_0 += alpha[i]*y[i]
    return theta, theta_0

def checkAlgo(x,y,theta,theta_0):
    for i in range(x.shape[0]):
        if y[i]*(np.dot(theta,x[i])+ theta_0) <= 0:
            return False
    return True



if __name__ =="__main__":
    x= np.array([[0,0],[2,0],[1,1],[0,2],[3,3],[4,1],[5,2],[1,4],[4,4],[5,5]])
    y= np.array([-1,-1,-1,-1,-1,1,1,1,1,1])
    alpha= np.array([1,65,11,31,72,30,0,21,4,5])
    phi = phiConversion(x)
    theta, theta_0 = calculatePerceptron(phi,y,alpha)
    print(theta,theta_0)
    print("Does Linear work:   ", checkAlgo(phi,y,theta,theta_0))