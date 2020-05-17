from sympy import *
import numpy as np

p,v= symbols('p v')

init_printing(use_unicode=True)

V = np.zeros(3)

actio = np.array([[0,1,0],[0,p,1-p],[0,0,1]])

reward = np.array([[0,0,0],[0,1,1],[0,0,0]])

for _ in range(2):
    C_action = np.sum(actio*(v*np.ones((3,3))*V[None,:]+reward),axis=1)
    V = C_action
    print(C_action)
