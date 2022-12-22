from sympy import *

def giai_dh():
    print("Giai dao ham:")
    x=symbols("x")
    f=(2*x-1)/(x+2)
    kq=diff(f,x)
    kq=print(kq)
    return kq