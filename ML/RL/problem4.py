# Unit 5 Home work 6
#1. Value Iteration for Markov Decision Process
import numpy as np
V = np.array([0,0,0,0])
reward_down = np.array([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,10,0]],dtype=float)
reward_up= np.array([[0,1,0,0],[0,0,1,0],[0,0,0,10],[0,0,0,0]],dtype=float)
gamma = .75
up = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]],dtype=float)
down = np.array([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]],dtype=float)




for i in range(0,100):
    up_action = np.sum(up*(gamma*np.ones((4,4))*V[None,:]+reward_up),axis=1)
    # print("up_action", up_action)
    down_action = np.sum(down*(gamma*np.ones((4,4))*V[None,:]+reward_down),axis=1)
    # print("down_action",down_action)
    transition_choices = np.stack([up_action,down_action])
    V = np.max(transition_choices, axis=0)
    print(V)

