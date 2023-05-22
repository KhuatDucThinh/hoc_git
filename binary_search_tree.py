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
                self.left == Nut(key)
            else:
                self.left.insert(key)

        elif key > self.key:
            if self.right == None:
                self.right == Nut(key)
            else:
                self.right.insert(key)
        else:
            print(f'Bi trung khoa {key}')

class Binarysearchtree:
    def __init__(self, key=None):
        if key == None:
            self.origin = None
        else:
            self.origin = Nut(key)

    def insert(self, key):
        if self.origin == None:
            self.origin = Nut(key)
        else:
            self.origin.insert(key)

    def delete(self, key):
        nut_cha = None
        cha_con = None
        nut_ht= self.origin 
        while nut_ht != None:
            if nut_ht.key > key:
                nut_cha = nut_ht
                nut_ht = nut_ht.left
                cha_con = 'trai'
            elif nut_ht.key < key:
                nut_cha = nut_ht
                nut_ht=nut_ht.right 
                cha_con = 'phai'
            else:
                if nut_cha == None:
                    
                    if nut_ht.left == None and nut_ht.right == None:

                        self.origin = None
                    elif nut_ht.left == None:

                        self.origin = nut_ht.right
                    elif nut_ht.right == None:

                        self.origin = nut_ht.left 
                    else:
                        self.origin = nut_ht.right 
                        tam = self.origin 
                        while tam.left != None:
                            tam = tam.left
                        tam.left = nut_ht.left 

                elif nut_ht.left == None and nut_ht.right == None:

                    if cha_con == 'trai':
                        nut_cha.left = None
                    else:
                        nut_cha.right = None

                elif nut_ht.left == None:

                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.right 
                    else:
                        nut_cha.right = nut_ht.right 

                elif nut_ht.right == None:

                    if cha_con == 'trai':
                        nut_cha.left = nut_ht.left 
                    else:
                        nut_cha.right = nut_ht.left 
                else:

                    if cha_con == 'trai':
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





                        

    def browse(self, origin=0):
        # duyệt LNR
        nut_ht = origin
        if origin == 0:
            nut_ht = self.origin

        if nut_ht==None:
            return []
        else:
            kq = []

            

            kq_left = self.browse(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            kq.append(nut_ht.key)

            kq_right = self.browse(nut_ht.right)
            for x in kq_right:
                kq.append(x)

            return kq
        
    def browse1(self, origin=0):
        # duyệt NTP
        nut_ht = origin
        if origin == 0:
            nut_ht = self.origin

        if nut_ht==None:
            return []
        else:
            kq = []

            kq.append(nut_ht.key)

            kq_left = self.browse1(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            

            kq_right = self.browse1(nut_ht.right)
            for x in kq_right:
                kq.append(x)

            

            return kq
        
    def browse2(self, origin=0):
        # duyệt TPN
        nut_ht = origin
        if origin == 0:
            nut_ht = self.origin

        if nut_ht==None:
            return []
        else:
            kq = []

            

            kq_left = self.browse2(nut_ht.left)
            for x in kq_left:
                kq.append(x)

            

            kq_right = self.browse2(nut_ht.right)
            for x in kq_right:
                kq.append(x)

            kq.append(nut_ht.key)

            return kq
        
    
        
    def search(self, key):
        if self.origin == None:
            return
        
        nut_ht = self.origin
        kq = ''
        while(nut_ht != None and nut_ht.key != key):
            kq = kq + f'{nut_ht.key} -> '
            if key <= nut_ht.key:
                nut_ht = nut_ht.left
            else:
                nut_ht = nut_ht.right 

        if nut_ht == None:
            return None
        else:
            kq = kq + f'{nut_ht.key}'
            return kq
        
def main():
    SPT = 10

    tree = Binarysearchtree()

    print('chen vào cây')
    tap_gia_tri =set()
    from random import randint
    while len(tap_gia_tri) < SPT:
        gt = randint(0, 100)
        tap_gia_tri.add(gt)

    tap_gia_tri = list(tap_gia_tri)
    #tập giá trị = [66, 46, 84, 11, 81, 99, 36, 77, 83, 87]

    print('chen lan luot ', tap_gia_tri)
    for x in tap_gia_tri:
        tree.insert(x)

    kq = tree.browse()
    print(' duyệt cây theo LNR', kq)

    kq = tree.browse1()
    print(' duyệt cây theo NLR', kq)

    kq = tree.browse2()
    print(' duyệt cây theo LRN', kq)

    gt = 84
    print(f'xoa {gt}')
    tree.delete(gt)


    while True:
        nhap = input('Nhap vao khoa can tim')
        if nhap == '':
            break

        gt = int(nhap)
        kq = tree.search(gt)
        if kq == None:
            print(f'Khong tim thay {gt}')
        else:
            print(f'tim thay {gt}: {kq}')

if __name__ =='__main__':
    main()



        













