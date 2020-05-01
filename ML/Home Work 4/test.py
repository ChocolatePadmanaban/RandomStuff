import numpy as np
import em
import common

X = np.loadtxt("test_incomplete.txt")
X_gold = np.loadtxt("test_complete.txt")

K = 1
n, d = X.shape
seed = 0
print(X)
# TODO: Your code here
def Lowest_cost():
    for seedvalue in range(1):
        mixture, post = common.init(X,K,seedvalue)
        mixture, post, cost = em.run(X,mixture,post)
        cost= common.bic(X, mixture,cost)
        print("Naive Cost of k:",K,"and seed",seedvalue, "is cost:",cost)
    print(em.fill_matrix(X,mixture))

    
if __name__ =="__main__":
    Lowest_cost()