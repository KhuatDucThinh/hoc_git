import random

def san_sinh_so_ngau_nhien(n):
    mang = []
    for i in range(n):
        songaunhien=random.randint(0, 100)
        mang.append(songaunhien)
      #end for
    return mang
#end def

def sap_xep_tron(mang):
    if len(mang) > 1:
        giua = len(mang)//2
        mang_trai = mang[0:giua]
        mang_phai = mang[giua:]

        sap_xep_tron(mang_trai)
        sap_xep_tron(mang_phai)

        i = j = k = 0
        while(i < len(mang_trai) and j<len(mang_phai)):
            if mang_trai[i] < mang_phai[j]:
               mang[k] = mang_trai[i]
               i = i + 1
            else:
                mang[k] = mang_phai[j]
                j = j + 1
            k = k + 1

        while i < len(mang_trai):
            mang[k] = mang_trai[i]
            i = i + 1
            k = k + 1

        while j < len(mang_phai):
            mang[k] = mang_phai[j]
            j = j + 1
            k = k + 1
        #end while

def main():
    mang = san_sinh_so_ngau_nhien(9)
    print("Mang ban dau la:", mang)
    sap_xep_tron(mang)
    print("mang sau sap xep la:", mang)


if __name__=='__main__':
    main()









    