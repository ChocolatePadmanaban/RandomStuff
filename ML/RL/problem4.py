import numpy as np
V = np.array([0,0,0,0])
reward_down = np.array([1,1,10,0])
reward_up= np.array([0,1,1,10])
gamma = 1/3
up = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]],dtype=float)
down = np.array([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]],dtype=float)




for i in range(0,100):
    up_action = up@(gamma*V+reward_up)
    print("up_action", up_action)
    down_action = down@(gamma*V+reward_down)
    print("down_action",down_action)
    transition_choices = np.stack([up_action,down_action])
    V = np.max(transition_choices, axis=0)
    print(V)