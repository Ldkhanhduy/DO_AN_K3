from sympy import *

def giai_lim():
    print("Giai limit:")
    x=symbols("x")
    f=((x**3-3*x**2)**(1/3))+(x**2-2*x)**(1/2)
    kq=limit(f,x,oo)
    kq=print(kq)
    return kq