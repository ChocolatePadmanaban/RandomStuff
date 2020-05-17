import math

pi = math.pi
coordinates= [1.0,2,3,4,5,6,7,8,9,10]
coordinates= [pi*c for c in coordinates]
label= [-1,1,-1,1,-1,1,-1,1,-1,1]

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

def LinearPerceptronAlgo(x,y):
    theta,theta_0 = 0,0
    alpha= []
    for _ in range(1000):
        for i in get_order(len(x)):
            alpha_0= 0
            
            if y[i]*(np.dot(theta, x[i])+ theta_0) <= 0:
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


x_2 = np.array(coordinates)**2
x_100 = np.array(coordinates)**20
x_cos = np.cos(np.array(coordinates))
x_sin= np.sin(np.array(coordinates))

theta,theta_0,alpha = LinearPerceptronAlgo(x_sin,label)
print("is it working", checkAlgo(x_sin,label,theta,theta_0))