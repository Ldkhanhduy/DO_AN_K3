def tim_kiem(a):
    try:
        vitri=[]
        n=float(input("Nhập số n:"))
        for i in range(len(a)):
            if n==a[i]:
                vitri.append(i)
        if len(vitri)==0:
            print("Không tìm thấy số",n,"trong list")
        else:
            print("Các vị trí của",n,"trong list là:",vitri)
        return a
    except Exception as e:
        print(e)