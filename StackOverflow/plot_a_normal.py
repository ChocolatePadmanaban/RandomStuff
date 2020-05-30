import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mum = 3.89-3.66
sigmam = math.sqrt(2*.5)

# muw = 3.89
# sigmaw = math.sqrt(.5)
x = np.linspace(mum - 3*sigmam, mum  + 3*sigmam, 1000)
plt.plot(x, stats.norm.pdf(x, mum, sigmam),color="red")

plt.show()