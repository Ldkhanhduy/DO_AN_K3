import matplotlib.pyplot as d
from matplotlib import cm
from numpy import *


def hyperbolic1(x,y):
    # x, y = meshgrid(x, y)
    f1 = sqrt((x/3) ** 2 + (y/5) ** 2 -1)*2

    # fig, ax = d.subplots(subplot_kw={"projection": "3d"})
    # ax.plot_surface(x, y, f1, cmap='Blues', linewidth=0, antialiased=False)
    # ax.plot_surface(x, y, f2, cmap='Blues', linewidth=0, antialiased=False)
    # ax.set_zlim(-8,8)
    # d.show()
    return f1

def hyperbolic2(x,y):
    f2 = -sqrt((x / 3) ** 2 + (y / 5) ** 2 - 1) * 2
    return f2
