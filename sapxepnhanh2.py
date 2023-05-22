import  random

def so_ngau_nhien(n):
    mang = []
    for i in range(n):
        stn= random.randint(0,100)
        mang.append(stn)
    return mang

def sap_xep_nhanh(mang):
    if len(mang) > 1:
        nho_hon=[]
        bang=[]
        lon_hon=[]

        p = mang[0]
        for x in mang:
            if x<p:
                nho_hon.append(x)
            elif x == p:
                bang.append(x)
            else:
                lon_hon.append(x)
        return sap_xep_nhanh(nho_hon) + bang + sap_xep_nhanh(lon_hon)
    


    else:
        return mang
    
def main():
    mang = so_ngau_nhien(10)
    print("mang ban dau la ", mang)
    mang = sap_xep_nhanh(mang)
    print("mang sau khi sap xep", mang)

if __name__=='__main__':
    main()