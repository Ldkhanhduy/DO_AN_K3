

def sap_xep(a):
    try:
        v=input("nhap 'True' neu muon sap xep tang dan,'False neu muon giam dan:")
        if v=="True":
            print('list sau khi sap xep theo chieu tang dan:')
            a=sorted(a,reverse=False)
        elif v=='False':
            print('List sau khi xap xep theo chieu giam dan:')
            a=sorted(a,reverse=True)
        print('a=',a)
        return a
    except Exception as e:
        print(e)
