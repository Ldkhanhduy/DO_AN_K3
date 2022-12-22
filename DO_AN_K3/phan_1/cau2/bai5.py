from phan_1.cau2 import bai1,bai2,bai3,bai4

def thuchien():
    nguon=input("Nhập tên tập tin cần lưu(cả nguồn):")
    a=float(input("Nhập a:"))
    b=float(input("Nhập b:"))
    v=bai1.sinh_list(a,b)
    bai4.luu(nguon,v)
    s=bai2.sap_xep(v)
    bai4.luu(nguon,s)
    bai3.tim_kiem(s)

if __name__=='__main__':
    thuchien()