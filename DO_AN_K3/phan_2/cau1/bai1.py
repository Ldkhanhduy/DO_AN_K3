import numpy as np
from taomatran import *

def tinh():
    print("Bai 1:")
    N=abs(int(input("nhap so phan tu cua vector x:")))
    x=tao_ma_tran(N,1)
    print("x=",x)
    m=abs(int(input("Nhap so hang cho ma tran A:")))
    n=abs(int(input("Nhap so cot cho ma tran A:")))
    while N!=n:
        n=abs(int(input("So cot cua A phai bang so phan tu cua x:")))
    else:
        A=tao_ma_tran(m,n)
        print("A=",A)
        tich=np.dot(A,x)
        tich=print("A.x=",tich)
    return tich
