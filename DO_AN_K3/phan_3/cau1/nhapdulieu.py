from employ import NhanVien

def nhap_vao_list(a:list):
    try:
        print("Nhap du lieu vao list:")
        n=abs(int(input("So nhan vien:")))
        for i in range(n):
            ten=input("Nhap ten:")
            tuoi=int(input("Nhap tuoi:"))
            luong=float(input("Muc luong:"))
            nv=NhanVien(ten,tuoi,luong)
            a.append(nv)
        return a
    except Exception as e:
        print(e)