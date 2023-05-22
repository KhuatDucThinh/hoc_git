import random 
def san_sinh_mang_ngau_nhien(n):
    mang = []

    for i in range(n):
        so_ngau_nhien= random.randint(0, 100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_noi_bot(mang):
    n = len(mang)

    for i in range(n): # i= 0 đến n -1
        

        for j in range(n - 2, i-1, -1):# j =[n-2, i]
            if mang[j] > mang[j +1]:
                mang[j], mang[j+1] = mang[j+1], mang[j]
                tiep_tuc = True
        print(i + 1, '-', mang)
        
        if tiep_tuc == False:
            break

def main():
    mang = san_sinh_mang_ngau_nhien(10)

    print("mang ban dau la:\n", mang)
    sap_xep_noi_bot(mang)
    print("mang sau khi sx là\n", mang)

if __name__ == '__main__':
    main()





