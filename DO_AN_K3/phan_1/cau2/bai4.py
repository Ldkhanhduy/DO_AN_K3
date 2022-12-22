from bai1 import *

def luu(nguon:str,a):
    try:
        n=input("Chọn kiểu lưu 'w' hoặc 'wb' cho tập tin:")
        if n=="w":
            a=str(a)
            with open(nguon,n) as f:
                f.write(a)
        if n=="wb":
            a=bytearray(a)
            with open(nguon,n) as f:
                f.write(a)
        print('Đã lưu list vào file mode=', n)
    except Exception as e:
        print(e)