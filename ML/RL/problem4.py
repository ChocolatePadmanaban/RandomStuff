#Re working on problem 2
import numpy as np

# row -> initial state , column -> destination state and extention -> actions 

transition_matrix= np.array([[[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]]])


transition_matrix = transition_matrix 
print(transition_matrix)
reward = np.array([0,0,0,0,1])

V_star = np.zeros(5)

def Value_iteration (transition_matrix, reward, V_star, g=.5 ):
    multiplier= reward+ g*V_star
    V_star= np.sum( multiplier * transition_matrix, axis=1)
    return V_star

for i in range(100):
    V_star=Value_iteration (transition_matrix, reward, V_star )
    print(V_star)