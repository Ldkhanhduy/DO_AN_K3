import os
import pickle
from employ import NhanVien

def ghi(thumuc: str, tentaptin: str, objs:list[NhanVien]):
    try:
        print("Luu vao tap tin:")
        with open(os.path.join(thumuc,tentaptin),'wb') as f:
            pickle.dump(objs,f)
        print('Da luu xong')
    except Exception as e:
        print("Loi")