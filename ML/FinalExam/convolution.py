import numpy as np
convolve = np.convolve
u=[2,1,-3,2,1]
v=[1,0,-1]
print(convolve([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]))
print(convolve([1,2,3,4,5,6,7,8,9],[1,2,3,4,5]))
print(convolve(u,v,mode='valid'))
print(convolve(v,u,mode='valid'))
