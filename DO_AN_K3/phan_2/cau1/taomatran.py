import numpy as np

def tao_ma_tran(a,b):
    x=np.random.uniform(-5,5,a*b).reshape(a,b)
    return x