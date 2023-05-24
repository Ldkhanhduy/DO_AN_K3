import pandas as p
import random as r

def sample(link):
    ga = p.read_csv(link, index_col=None)
    mau = p.DataFrame(ga[1:2])
    a = r.sample(range(5000), 500)
    for i in range(len(a)):
        mau = mau.append(ga[a[i]-1:a[i]])
    mau = mau.drop(1)
    mau.to_excel("D:/Duy/honda_sample.xlsx")
    print("Mẫu lấy được:")
    print(mau)

if __name__ == '__main__':
    a = "D:/Baitap/BT_EXCEL/honda_sell_data.csv"
    sample(a)