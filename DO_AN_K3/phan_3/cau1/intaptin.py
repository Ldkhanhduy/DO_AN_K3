import os
import pickle

def doc(thumuc: str, tentaptin:str):
    try:
        print("In ra man hinh:")
        with open(os.path.join(thumuc,tentaptin),'rb') as f:
            a=pickle.load(f)
        for i in a:
                print(i)
    except Exception as e:
        print(e)
        return None