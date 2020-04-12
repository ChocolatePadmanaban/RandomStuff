import numpy as np 

def CostClaculator(x,z):
    temp = [ (np.linalg.norm(x_i-z))**2    for x_i in x]
    return sum(temp)

if __name__ == "__main__":
    x1= np.array([[-1,2],[-2,1],[-1,0]])
    z1= np.array([-1,1])
    x2= np.array([[2,1],[3,2]])
    z2= np.array([2,2])

    print(CostClaculator(x1,z1))
    print(CostClaculator(x2,z2))
    print(CostClaculator(x1,z1)+CostClaculator(x2,z2))
