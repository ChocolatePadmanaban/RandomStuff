import numpy as np

def ReLu1(x):
    return max(x,0)
Relu = np.vectorize(ReLu1)
def NeuralNetowrks(W,V,X):
    Z= np.dot(W,X)
    print(Z)
    F= Relu(Z)
    F = np.append(F,[1])
    U= np.dot(V,F)
    
    U= Relu(U)
    return Sofmax(U)

def Sofmax(U):
    U= np.exp(U)
    dividentcolom = np.sum(U,axis=0)
    return np.divide(U,dividentcolom)
    
if __name__=="__main__":
    w=np.array([[1,0,-1],[0,1,-1],[-1,0,-1],[0,-1,-1]])
    x=np.array([3,14,1])
    v= np.array([[1,1,1,1,0],[-1,-1,-1,-1,2]])
    print(NeuralNetowrks(w,v,x))