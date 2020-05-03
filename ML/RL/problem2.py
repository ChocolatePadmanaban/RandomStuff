#Value iteration with different tansition matrix
import numpy as np

# row -> initial state , column -> destination state and extention -> actions 

transition_matrix= np.array([[0., 1, 0., 0., 0.],
       [0., 0., 1, 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1],
       [0., 0., 0., 0, 1]])


transition_matrix = transition_matrix / np.sum(transition_matrix,axis=1)
print(transition_matrix)
reward = np.array([0,0,0,0,1])

V_star = np.zeros(5)

def Value_iteration (transition_matrix, reward, V_star, g=.5 ):
    multiplier= reward+ g*V_star
    V_star= np.sum(transition_matrix * multiplier, axis=1)
    return V_star

for i in range(100):
    V_star=Value_iteration (transition_matrix, reward, V_star )
    print(V_star)

