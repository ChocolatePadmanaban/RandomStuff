import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")

def Lowest_cost():
    K= [1,2,3,4]
    for k in K:
        minimumcost= np.inf
        for seedvalue in range(5):
            mixture, post = common.init(X,k,seedvalue)
            mixture, post, cost = naive_em.run(X,mixture,post)
            cost= common.bic(X, mixture,cost)
            minimumcost = min(cost,minimumcost)
        print("Naive Cost of k:",k,"is cost:",minimumcost)
        common.plot(X,mixture,post,"Naive Cost of k:"+str(k)+"is cost:"+str(minimumcost))
    for k in K:
        minimumcost= np.inf
        for seedvalue in range(5):
            mixture, post = common.init(X,k,seedvalue)
            mixture, post, cost = kmeans.run(X,mixture,post)
            minimumcost = min(cost,minimumcost)
        print("kmeans Cost of k:",k,"is cost:",minimumcost)
        common.plot(X,mixture,post,"kmeans Cost of k:"+str(k)+"is cost:"+str(minimumcost))

if __name__ =="__main__":
    Lowest_cost()
