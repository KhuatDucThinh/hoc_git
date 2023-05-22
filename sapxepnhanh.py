import random

def sansinhsongaunhien(n):
    mang = []
    for i in range(n):
     songaunhien=random.randint(0, 100)
     mang.append(songaunhien)
    return mang

def phan_chia_vung(mang, duoi, tren):
   i = duoi - 1# chỉ mức của phần tử nhỏ hơn mốc
   moc = mang[tren] 
   #Dua lan luot cac phan tu nho hon moc ve tren
   for j in range(duoi, tren):
      if mang[j]< moc:
         i = i + 1
         mang[i], mang[j] = mang[j], mang[i]


   mang[i + 1], mang[tren] = mang[tren], mang[i + 1]

   return i + 1

def sap_xep_nhanh(mang, duoi, tren):
   if duoi < tren :
      vitri = phan_chia_vung(mang, duoi, tren)
      sap_xep_nhanh(mang, duoi, vitri - 1)
      sap_xep_nhanh(mang, vitri + 1, tren)


def main():
   mang = sansinhsongaunhien(10)
   print("mang ban dau la ", mang)
   sap_xep_nhanh(mang, 0, len(mang) - 1)
   print("mang sau khi sx", mang)

if __name__ =='__main__':
   main()

   



