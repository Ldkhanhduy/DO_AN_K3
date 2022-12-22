from nhapdulieu import *
from indulieu import *
from xapsep import *
from luutaptin import *
from intaptin import *

def main():
    nguon="D:/data"
    ten="file.txt"
    a=[]
    nhap_vao_list(a)
    in_du_lieu(a)
    xap_sep(a)
    ghi(nguon,ten,a)
    doc(nguon,ten)

if __name__=='__main__':
    main()