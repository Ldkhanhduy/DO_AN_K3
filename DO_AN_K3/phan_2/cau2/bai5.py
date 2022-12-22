from sympy import *

def giai_tp():
    print("Giai tich phan:")
    x=symbols('x')
    f=((1-x*tan(x))/(x**2-cos(x)+x))
    kq=integrate(f,(x,(2*pi)/3,pi))
    print(kq)
