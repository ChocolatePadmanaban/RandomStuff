# import random
# import matplotlib.pyplot as plt 
# import matplotlib.animation as animation
# from matplotlib import style


# #people = ['Newton', 'Maxwell', 'Gauss', 'Pythogarus', 'Leibniz', 'Reimann','Taylor', 'Fibonnaci', 'Napier', 'Bernoulli']
# people = [i for i in range(10)]
# peoplewithmoney= [10  for person in people]
# print(peoplewithmoney)

# # plt.bar(peoplewithmoney.keys(), peoplewithmoney.values(), color='g')
# # plt.show()

# def Trade(Peoplewithmoney, therepeat=1):
#     ims = []
#     fig = plt.figure()
#     People_index=[i for i in range(len(Peoplewithmoney))]
#     for r in range(therepeat):
#         for i in range(len(People_index)):
#             reciver, loser = random.sample(People_index,2)
#             if Peoplewithmoney[reciver] < 1:
#                 People_index.remove(reciver)
#             elif Peoplewithmoney[loser] < 1:
#                 People_index.remove(loser)
#             else:
#                 Peoplewithmoney[reciver]+=1
#                 Peoplewithmoney[loser]-=1
                            
#             im= plt.imshow(Peoplewithmoney, animated=True)
#             ims.append([im])
#     ani = animation.ArtistAnimation(fig, ims, interval=50, blit= True,
#                     repeat_delay=1000)
#     plt.show()

# if __name__ == "__main__":
#     Trade(peoplewithmoney,1)


"""
==================
Animated histogram
==================

Use a path patch to draw a bunch of rectangles for an animated histogram.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)

 
people_money = [100 for _ in range(1000)]


# histogram our data with numpy
data = people_money
n, bins = np.histogram(data, bins=100)

# get the corners of the rectangles for the histogram
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

###############################################################################
# Here comes the tricky part -- we have to set up the vertex and path codes
# arrays using `.Path.MOVETO`, `.Path.LINETO` and `.Path.CLOSEPOLY` for each
# rect.
#
# * We need 1 ``MOVETO`` per rectangle, which sets the initial point.
# * We need 3 ``LINETO``'s, which tell Matplotlib to draw lines from
#   vertex 1 to vertex 2, v2 to v3, and v3 to v4.
# * We then need one ``CLOSEPOLY`` which tells Matplotlib to draw a line from
#   the v4 to our initial vertex (the ``MOVETO`` vertex), in order to close the
#   polygon.
#
# .. note::
#
#   The vertex for ``CLOSEPOLY`` is ignored, but we still need a placeholder
#   in the ``verts`` array to keep the codes aligned with the vertices.
nverts = nrects * (1 + 3 + 1)
verts = np.zeros((nverts, 2))
codes = np.full(nverts, path.Path.LINETO)
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

###############################################################################
# To animate the histogram, we need an ``animate`` function, which generates
# a random set of numbers and updates the locations of the vertices for the
# histogram (in this case, only the heights of each rectangle). ``patch`` will
# eventually be a `.Patch` object.
patch = None

def Radom_trade():
    global people_money
    people_money = np.sort(people_money)
    positve_start = len(people_money[people_money > 0])
    print(positve_start)
    for _ in people_money:
        giver, reciver = np.random.choice(positve_start, 2, replace=False)
        people_money[len(people_money)-giver-1]+=1
        people_money[len(people_money)-reciver-1]-=1
    print(np.median(people_money))
    print(people_money)





def animate(i):
    
    Radom_trade()
    data = people_money
    n, bins = np.histogram(data, bins=100)
    top = bottom + n
    verts[1::5, 1] = top
    verts[2::5, 1] = top
    return [patch, ]

###############################################################################
# And now we build the `.Path` and `.Patch` instances for the histogram using
# our vertices and codes. We add the patch to the `~.axes.Axes` instance, and
# setup the `.FuncAnimation` with our ``animate`` function.
fig, ax = plt.subplots()
barpath = path.Path(verts, codes)
patch = patches.PathPatch(
    barpath, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True)
plt.show()
