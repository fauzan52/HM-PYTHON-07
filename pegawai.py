from staff import Staff

class Dosen(Staff):
    jabatan = 'Dosen'
    def __init__(self, nama, alamat,nip):
        self.nip = nip
        self.gaji = 5000000
        super().__init__(nama,alamat)
     
    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nip, self.gaji, self.jabatan)


class Admin(Staff):
    jabatan = 'Admin'
    def __init__(self, nama, alamat, nip,gaji):
        self.nip = nip
        self.gaji = gaji
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nip, self.gaji, self.jabatan)
    

class CleaningServis(Staff):
    jabatan = 'Cleaning Service'
    gaji = "Staff ats"
    def __init__(self, nama, alamat, nipCS):
        self.nipCS = nipCS
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nipCS, self.gaji, self.jabatan)
    
printdosen = Dosen('Bambang','Tegal','987836')
print(printdosen) 
printadmin = Admin('Anisa', 'Aceh', '900006',4500000)
print(printadmin)
printcs = CleaningServis('sukarmi','Sulawesi','679972')
print(printcs)
