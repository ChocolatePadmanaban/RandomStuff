import numpy as np
import em
import common

X = np.loadtxt("test_incomplete.txt")
X_gold = np.loadtxt("test_complete.txt")

K = 6
n, d = X.shape
seed = 0

# TODO: Your code here
def Lowest_cost():
    mixture, post = common.init(X,K)
    mixture, post, cost = em.run(X,mixture,post)
    cost= common.bic(X, mixture,cost)
    print("Naive Cost of k:",K,"is cost:",cost)
    
if __name__ =="__main__":
    Lowest_cost()