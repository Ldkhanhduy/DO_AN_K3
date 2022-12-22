from sympy import *

x=symbols('x')
f=x**4-2*x**2-3
def d2():
    x=symbols('x')
    d=diff(f,x)
    return d

def d3():
    x=symbols('x')
    f=diff(d2(),x)
    return f

def d4():
    x=symbols('x')
    f=diff(d3(),x)
    return f

def main():
    x=symbols('x')
    y1=d2()
    y2=d3()
    y3=d4()
    a=plot(f,y1,y2,y3,(x,-10,10,200),xlabel=r'$x$',ylabel=r'$y$')
    a.show()

if __name__=='__main__':
    main()