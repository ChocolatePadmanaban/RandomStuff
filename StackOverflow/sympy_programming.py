
import sympy as sy
import numpy as np
from sympy.plotting import plot
x = sy.symbols('x')
f = sy.sin(x)
x_array = np.linspace(0, np.pi, 1000)
f_array = sy.lambdify(x, f)(x_array)
plot(f, (x, 0, sy.pi), fill={'x': x_array,'y1':f_array,'color':'green'})

