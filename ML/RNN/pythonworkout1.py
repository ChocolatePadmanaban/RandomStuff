import math

def sigmoid(x):
    if x>=1:
        return 1
    elif x<=-1:
        return 0
    return 1/(1+math.exp(-x))

def tanh(x):
    if x>=1:
        return 1
    elif x<=-1:
        return -1
    return math.tanh(x)

def LSTM(X):
    h_1= 0
    H =[]
    for x in X:
        o_t= sigmoid(100*x)
        c_t= tanh(-100*h_1+50*x)
        h_1 = int(o_t*tanh(c_t))
        H.append(h_1)
    return H

if __name__ == "__main__":
    print(LSTM([1,1,0,1,1]))