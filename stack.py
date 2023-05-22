class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None


class dslienket:
    def __init__(self):
        self.dau = None
        self.duoi = None


    def __str__(self):
        kq = ''
        stt = 0
        hien_tai = self.dau 
        while hien_tai != None:
            stt = stt + 1
            if stt == 1:
                kq = kq + str(hien_tai.gia_tri)
            else:
                kq = kq + '->' + str(hien_tai.gia_tri)

            hien_tai = hien_tai.nut_ke_tiep

        return kq
    
def them_dau(self, gia_tri):
    nut = Nut(gia_tri)
    if self.dau == None:
        self.dau = nut
        self.duoi = nut
    else:
        nut.nut_ke_tiep = self.dau
        self.dau = nut


def them_duoi (self, gia_tri):
    nut = Nut(gia_tri)
    if self.dau == None:
        self.dau = nut
        self.duoi = nut
    else:
        self.duoi.nut_ke_tiep = nut
        self.duoi = nut

def lay_dau(self):
    if self.dau == None:
        return None
    else:
        return self.dau.gia_tri

def xoa_dau(self):
    tam = self.dau
    if self.dau == self.duoi:
        self.dau = None
        self.duoi = None
    else:
        self.dau = self.dau.nut_ke_tiep
        
    del tam    


