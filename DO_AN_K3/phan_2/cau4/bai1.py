import matplotlib.pyplot as d
import numpy as np
from matplotlib import cm

def yen_ngua(x,y):
    # x,y=np.meshgrid(x,y)
    f = (x/3)**2-(y/2)**2
    # fig,ax=d.subplots(subplot_kw={"projection":"3d"})
    # ax.plot_surface(x,y,f,cmap=cm.coolwarm,linewidth=0,antialiased=False)
    # ax.set_zlim(-70,25)
    # d.show()
    return f