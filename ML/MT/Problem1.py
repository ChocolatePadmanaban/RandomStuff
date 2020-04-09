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

def calculatePerceptron(x,y,alpha):
    theta,theta_0 = np.zeros([1,2]),0
    for i in range(x.shape[0]):
        theta += alpha[i]*y[i]*x[i]
        theta_0 += alpha[i]*y[i]
    return theta, theta_0

def LinearPerceptronAlgo(x,y):
    theta,theta_0 = np.zeros([1,2]),0
    alpha= []
    for _ in range(100):
        for i in get_order(x.shape[0]):
            alpha_0= 0
            
            if y[i]*(np.dot(theta, x[i])+ theta_0) <= 0:
                theta += y[i]*x[i]
                theta_0 += y[i]
                alpha_0+=1
            alpha.append(alpha_0)
    return theta, theta_0, alpha

def Maximizemargin(x,y):
    theta,theta_0 = np.zeros([1,2]),0
    alpha= []
    for _ in range(100):
        for i in get_order(x.shape[0]):
            alpha_0= 0
            
            if y[i]*(np.dot(theta, x[i])[0]+ theta_0) <= 1:
                theta += y[i]*x[i]
                theta_0 += y[i]
                alpha_0+=1
            alpha.append(alpha_0)
    return theta, theta_0, alpha

def checkAlgo(x,y,theta,theta_0):
    for i in range(x.shape[0]):
        if y[i]*(np.dot(theta,x[i])+ theta_0) <= 1:
            return False
    return True

def hindgeloss(x,y,theta,theta_0):
    dummy = 1-y*(np.dot(x,theta[0])+theta_0)
    print(dummy)
    return max(0, dummy)


def SumHindgeLoss(x,y,theta,theta_0):
    loss_list = [hindgeloss(x[i],y[i],theta,theta_0)  for i in range(x.shape[0])]
    return sum(loss_list)




if __name__ =="__main__":
    x= np.array([[0,0],[2,0],[3,0],[0,2],[2,2],[5,1],[5,2],[2,4],[4,4],[5,5]])
    y= np.array([-1,-1,-1,-1,-1,1,1,1,1,1])
    alpha= np.array([1,9,10,5,9,11,0,3,1,1])
    theta, theta_0 ,dummy= Maximizemargin(x,y)
    print(theta,theta_0)
    print("Does Linear work:   ", checkAlgo(x,y,theta,theta_0))
    print("the sum of hidnge loss is ", SumHindgeLoss(x,y,theta/2,theta_0/2))