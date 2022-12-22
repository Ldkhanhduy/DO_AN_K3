import numpy as np
from taomatran import *

def tinh2():
    print("Bai 2:")
    m=abs(int(input("Nhap so hang cho ma tran A, B:")))
    n=abs(int(input("Nhap so cot cho ma tran A, B:")))
    A=tao_ma_tran(m,n)
    print("A=",A)
    B=tao_ma_tran(m,n)
    print("B=",B)
    print("Phep nhan Hadamard:")
    hadamard=np.multiply(A,B)
    hadamard=print("AoB=",hadamard)
    print("Phep nhan hai ma tran:")
    C=A.copy()
    C=C.T
    tich=np.dot(C,B)
    tich=print("A*B",tich)
    return hadamard,tich