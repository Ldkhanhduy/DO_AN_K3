from sympy import *

def giai_nh():
    print("Giai nguyen ham:")
    x=symbols("x")
    f=x/(x**2-1)
    kq=integrate(f,x)
    kq=print(kq)
    return kq