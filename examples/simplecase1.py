import sys
sys.path.append('..')

import matplotlib.pyplot as plt
from matplotlib import animation

import numpy as np
from Gimli.World import World

def func(own,up,down,left,right,upright,downright,upleft,downleft):
    sum = up + down + left + right + upright + downright + upleft + downleft
    return 1*(sum==3) or own*(sum==2)

world = World(func,[100,100])
cells = -world.getcells()

fig = plt.figure()
im = plt.imshow(cells,interpolation='none',cmap='gray')


def animate(i):
    world.update()
    cells = -world.getcells()
    im.set_array(cells)
    return [im]

anim = animation.FuncAnimation(fig,animate,frames=200, interval=60, blit=True)
plt.show()