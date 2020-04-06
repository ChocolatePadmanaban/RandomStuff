import numpy as np
def Convolution(f,g_):
    m,n=g_.shape
    g=g_.flatten()
    answermatrix=[]
    for i in range(f.shape[0]-m+1):
        tempmat=[]
        for j in range(f.shape[1]-n+1):
            tempmat.append(np.dot(f[i:i+m,j:j+n].copy().flatten(),g))
        answermatrix.append(tempmat)
    print(answermatrix)
    return np.sum(answermatrix)

if __name__ =="__main__":
    f= np.array([[1,0,2],[3,1,0],[0,0,4]])
    g=np.array([[1,0],[0,1]])
    print(Convolution(f,g))