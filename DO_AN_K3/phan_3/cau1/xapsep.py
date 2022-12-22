def xap_sep(a):
    try:
        print("Xap sep list")
        a = sorted(a, reverse=False)
        print("Sau khi xap sep theo do tuoi:")
        for i in a:
            print(i)
    except Exception as e:
        print(e)