class Nut:
    
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None


    def insert(self, key):
        if self is None:
            nut = Nut(key)
            self = nut
            return
        
        if key < self.key:
            if self.left == None:
                self.left = Nut(key)
            else:
                self.left.insert(key)

        elif key > self.key:
            if self.right == None:
                self.right = Nut(key)
            else:
                self.right.insert(key)

        else:
            print(f'Bị trùng khóa {key}')


class Binary_search_tree:
    
    def __init__(self, key=None):
        if key ==None:
            self.origin = None
        else:
            self.origin = Nut(key)

    
    def insert(self, key):
        if self.origin == None:
            self.origin = Nut(key)
        else:
            self.origin.insert(key)

    
    def delete(self, key):
        nut_cha =None
        cha_con = None
        nut_ht = self.origin 

        while nut_ht != None:
            if nut_ht.key > key:
                nut_cha=nut_ht
                nut_ht = nut_ht.left 
                cha_con = 'left'
            elif nut_ht.key < key:
                nut_cha = nut_ht 
                nut_ht = nut_ht.right 
                cha_con = 'right'
            else: #tìm thấy
                if nut_cha == None:
                    #xóa nút gốc
                    if nut_ht.left == None and nut_ht.right == None:
                        #xóa nút gốc k có con
                        self.origin = None
                    elif nut_ht.left == None :
                        #xóa nút gốc chỉ có 1 nút con bên phải
                        self.origin = nut_ht.right 
                    elif nut_ht.right == None:
                        #xóa nút gốc chỉ có 1 con bên trái
                        self.origin = nut_ht.left 
                    else:
                        #xóa nút  gốc có đủ 2 con
                        #xoay trái
                        self.origin = nut_ht.right 
                        tam = self.origin 
                        while tam.left != None:
                            tam = tam.left 

                        tam.left = nut_ht.left 

                elif nut_ht.left == None and nut_ht.right == None:
                    #xóa nút lá
                    if cha_con == 'left':
                        nut_cha.left = None 
                    else:
                        nut_cha.right = None

                elif nut_ht.left == None:
                    #xóa nút chỉ có 1 con bên phải
                    if cha_con == 'left':
                        nut_cha.left = nut_ht.right 
                    else:
                        nut_cha.right = nut_ht.right 
                
                elif nut_ht.right == None:
                    #xóa nút chỉ có 1 con bên trái
                    if cha_con == 'left':
                        nut_cha.left = nut_ht.left 
                    else:
                        nut_cha.right = nut_ht.left 
                else:
                    #xóa nút có đủ 2 con
                    #xoay trái
                    if cha_con == 'left':
                        nut_cha.left = nut_ht.right 
                    else:
                        nut_cha.right = nut_ht.right 


                    if nut_ht.right.left == None:
                        nut_ht.right.left = nut_ht.left 
                    else:
                        tam = nut_ht.right 
                        while tam.left != None:
                            tam = tam.left 
                        
                        tam.left = nut_ht.left 
                
                del nut_ht 
                break




        

    
    def browser(self, origin=0):
        #duyệt theo LNR
        nut_ht= origin
        if origin == 0:
            nut_ht = self.origin 
            
        if nut_ht == None:
            return []
        else:
            kq = []

            kq_left = self.browser(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            kq.append(nut_ht.key)

            kq_right = self.browser(nut_ht.right)
            for x in kq_right:
                kq.append(x)
            
            return kq

    def browser1(self, origin=0):
        #duyệt theo NLR
        nut_ht= origin
        if origin == 0:
            nut_ht = self.origin 
            
        if nut_ht == None:
            return []
        else:
            kq = []

            kq.append(nut_ht.key)

            kq_left = self.browser1(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            

            kq_right = self.browser1(nut_ht.right)
            for x in kq_right:
                kq.append(x)
            
            return kq    
    
    def browser2(self, origin=0):
        #duyệt theo LRN
        nut_ht= origin
        if origin == 0:
            nut_ht = self.origin 
            
        if nut_ht == None:
            return []
        else:
            kq = []

            

            kq_left = self.browser2(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            

            kq_right = self.browser2(nut_ht.right)
            for x in kq_right:
                kq.append(x)

            kq.append(nut_ht.key)
            
            return kq 
        
    def search(self, key):
        if self.origin == None:
            return
        
        
        nut_ht = self.origin 
        kq = ''
        while (nut_ht != None and nut_ht.key != key):
            kq = kq + f'{nut_ht.key} ->'
            if key <= nut_ht.key:
                nut_ht= nut_ht.left 
            else:
                nut_ht = nut_ht.right 

        
        if nut_ht == None :
            return None
        else:
            kq = kq + f'{nut_ht.key}'
            return kq
        
def main():
    SPT = 10
    tree = Binary_search_tree()

    print('===== Chèn vào cây=====')
    tap_gia_tri = set()
    from random import randint 
    while len(tap_gia_tri) < SPT:
        gt = randint(0, 100)
        
        tap_gia_tri.add(gt)

    tap_gia_tri = list(tap_gia_tri)
    tap_gia_tri = [66, 46, 84, 11, 81, 99, 36, 77, 83, 87, 100, 86, 85]

    print('chèn lần lượt', tap_gia_tri)

    for x in tap_gia_tri:
            tree.insert(x)

    kq = tree.browser()
    print(' Duyệt cây theo LNR', kq)
    kq=tree.browser1()
    print('duyệt cây theo NLR', kq)
    kq=tree.browser2()
    print('duyệt cây theo LRN', kq)
    
    gt= 84
    print(f'Xóa {gt}')
    tree.delete(gt)
    
    while True:
        nhap = input('Nhập vào khóa cần tìm: ')
        if nhap == '':
            break

        gt = int(nhap)
        kq = tree.search(gt)
        if kq == None:
            print(f'Không tìm thấy {gt}')
        else:
            print(f'Tìm thấy {gt}: {kq}')

if __name__=='__main__':
    main()




        

        
    
