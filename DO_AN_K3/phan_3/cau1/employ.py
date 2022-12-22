class NhanVien:
    def __init__(self,hoten:str,tuoi:int,luong:float):
        self.hoten=hoten
        self.tuoi=tuoi
        self.luong=luong

    def __str__(self)->str:
        pt='[Ho ten:'+self.hoten+';tuoi:'+str(self.tuoi)+';luong:'+str(self.luong)+']'
        return pt

    def __gt__(self, other):
        return (self.tuoi>other.tuoi)

    def __ge__(self, other):
        return (self.tuoi>=other.tuoi)

    def __lt__(self, other):
        return (self.tuoi<other.tuoi)

    def __le__(self, other):
        return (self.tuoi<=other.tuoi)

    def __eq__(self, other):
        return (self.tuoi==other.tuoi)