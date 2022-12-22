import random as r

def sinh_list(a,b):
    try:
        n=abs(int(input("nhap so phan tu cho list:")))
        c=[((b+1-a)*r.random()+a) for i in range(n)]
        for i in range(len(c)):
            c[i]=round(c[i],1)
        print("a=",c)
        return c
    except Exception as e:
        print(e)