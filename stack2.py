from stack import dslienket

class NganXep:
    def __init__(self):
        self.danh_sach = dslienket()

    def la_rong(self):
        return self.danh_sach.dau == None
    
    def __str__(self):
        kq = 'Ngan Xep['
        kq = kq + str(self.danh_sach)
        kq = kq + ']'
        return kq
    def day_vao(self, gia_tri):
        self.danh_sach.them_dau(gia_tri)


    def lay_ra(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
        
if __name__ == '__main__':
    ngan_xep = NganXep()
    print(ngan_xep)

    print('---- day vao ------')
    for i in range(1, 6):
        print(f'day vao {i}')
        ngan_xep.day_vao(i)
        print(ngan_xep)

    

    

    
    