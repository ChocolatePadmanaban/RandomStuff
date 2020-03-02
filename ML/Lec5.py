import numpy as np

def HingeLoss(featureMatrix, labels, theta):
    n=len(labels)
    beforeLoss = [ labels[i]-np.dot(theta, featureMatrix[i]) for i in range(n) ]
    loss = [1-i if i< 1 else 0 for i in beforeLoss]
    return sum(loss)/n

def SquaredErrorLoss(featureMatrix, labels, theta):
    n=len(labels)
    loss = [ .5*(labels[i]-np.dot(theta, featureMatrix[i]))**2 for i in range(n)]
    #loss = [1-i if i< 1 else 0 for i in beforeLoss]
    return sum(loss)/n

if __name__ == "__main__":
    print(SquaredErrorLoss(
        np.array([[1,0,1],[1,1,1],[1,1,-1],[-1,1,1]]),[2,2.7,-0.7,2],[0,1,2]
    ))
