# Unit 5 Home work 6
#2. Q-Value Iteration

import numpy as np

V = np.zeros(6)

gamma = .6
M = np.array([[1,0,0,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]],dtype=float)
C = np.array([[1,0,0,0,0,0],[0,.3,0,.7,0,0],[0,0,.3,0,0.7,0],[0,0,0,.3,0,.7],[0,0,0,0,1,0],[0,0,0,0,0,1]],dtype=float)

reward = np.zeros((6,6))
for i in range(reward.shape[0]):
    for j in range(reward.shape[1]):
        if i != j:
            reward[i,j] = abs(j-i)**(1/3)
        else:
            if i!=0:
                reward[i,i] = (i+4)**(-1/2)
print("reward",reward)



for i in range(0,1):
    M_action = np.sum(M*(gamma*np.ones((6,6))*V[None,:]+reward),axis=1)
    print("M_action",M_action)
    C_action = np.sum(C*(gamma*np.ones((6,6))*V[None,:]+reward),axis=1)

    transition_choices = np.stack([M_action,C_action])
    print("transition_choices",transition_choices)
    V = np.max(transition_choices, axis=0)
    print(V)