import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

x = sy.symbols('x')
f = sy.sin(x)

x_array = np.linspace(0, np.pi, 1000)
f_array = sy.lambdify(x, f)(x_array)

fig, ax = plt.subplots()

ax.plot(x_array, f_array, color = 'red')
ax.fill_between(x_array, f_array, facecolor = 'red', alpha = 0.3)

plt.show()