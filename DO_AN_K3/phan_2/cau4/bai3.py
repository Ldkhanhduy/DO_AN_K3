from mpl_toolkits import mplot3d
from matplotlib import cm
import matplotlib.pyplot as d
import numpy as np

def hinh_cau1(x,y):
    # x, y = np.meshgrid(x, y)
    z1=(4-(x+2)**2-(y-1)**2)**(1/2)+4

    # fig, ax = d.subplots(subplot_kw={"projection": "3d"})
    # ax.plot_surface(x,y,z1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
    # ax.plot_surface(x, y, z2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # ax.set_zlim(2,6)
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # d.show()
    return z1

def hinh_cau2(x,y):
    z2 = -(4 - (x + 2) ** 2 - (y - 1) ** 2) ** (1 / 2) + 4
    return z2
