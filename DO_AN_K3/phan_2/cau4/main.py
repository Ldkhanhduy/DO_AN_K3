from phan_2.cau4 import bai1,bai2,bai3
import matplotlib.pyplot as d
from numpy import *
from matplotlib import cm

def main():
    try:
        fig,(ax1,ax2,ax3)=d.subplots(1,3,subplot_kw={"projection":"3d"})
        xa=linspace(-15,15,200)
        ya=linspace(-15,15,200)
        xb=linspace(-8,8,1000)
        yb=linspace(-8,8,1000)
        xc=linspace(-4,0,10500)
        yc=linspace(-1,3,10500)
        xa,ya=meshgrid(xa,ya)
        xb,yb=meshgrid(xb,yb)
        xc,yc=meshgrid(xc,yc)
        a=bai1.yen_ngua(xa,ya)
        b1=bai2.hyperbolic1(xb,yb)
        b2=bai2.hyperbolic2(xb,yb)
        c1=bai3.hinh_cau1(xc,yc)
        c2=bai3.hinh_cau2(xc,yc)
        ax1.plot_surface(xa,ya,a,cmap="Blues",linewidth=0,antialiased=False)
        ax2.plot_surface(xb,yb,b1,cmap="gray",linewidth=0,antialiased=False)
        ax2.plot_surface(xb, yb, b2, cmap="gray_r", linewidth=0, antialiased=False)
        ax3.plot_surface(xc, yc, c1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax3.plot_surface(xc, yc, c2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax1.set_zlim(-70,25)
        ax2.set_zlim(-8,8)
        ax3.set_zlim(2,6)
        d.show()
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()