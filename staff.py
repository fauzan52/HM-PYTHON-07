from stakeholder import SH

class Staff(SH):
    def __init__(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
        super().__init__(nama,alamat)
        
    def __str__(self):
        return '{} || {} '.format(self.nama,self.alamat)
    
if __name__ == '__main__':
    printstaff = Staff ('Adi','Jakarta')
    print(printstaff)
    