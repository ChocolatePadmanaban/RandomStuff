#Value iteration
import numpy as np

# row -> initial state , column -> destination state and extention -> actions 

transition_matrix= np.array([[[0.5, 2/3 + 1/6],
        [0.5, 1/6],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0.25, 1/6],
        [0.5, 2/3],
        [0.25, 1/6],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0.25, 1/6],
        [0.5, 2/3],
        [0.25, 1/6],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0.25, 1/6],
        [0.5, 2/3],
        [0.25, 1/6]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0.5, 1/6],
        [0.5, 2/3 + 1/6]]])


transition_matrix = transition_matrix 
print(transition_matrix)
reward = np.array([0,0,0,0,1])
reward = np.ones((5,5,2))*reward[None,:,None]
#reward[4,4,1]= 1
print(reward)
V_star= np.zeros(5)


def Value_iteration (transition_matrix, reward, V_star, g=.5 ):
    V_exec = np.ones((5,5,2))*V_star[None,: , None]
    #print("V_exec", V_exec)
    Q_star = np.sum(transition_matrix*(reward+ g*V_exec), axis=1)
    #print("Q_star",Q_star)
    return np.max(Q_star, axis=1)

  

for i in range(100):
    V_star=Value_iteration (transition_matrix, reward, V_star )
    print("V_star",V_star)

