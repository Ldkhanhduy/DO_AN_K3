from sympy import *

def giai_hpt():
    print("Giai he phuong trinh:")
    x,y,z=symbols("x,y,z")
    pt1= Eq(2*x-5*y+z,-5)
    pt2= Eq(4*x+2*y-2*z,2)
    pt3= Eq(x+y-z,0)
    kq = solve((pt1,pt2,pt3),(x,y,z))
    kq=print(kq)
    return kq
