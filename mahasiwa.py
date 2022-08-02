from pesertadidik import Mahasiswa 

class MahasiswaS1(Mahasiswa):
    jabatan = 'Mahasiswa S1'
    def __init__(self, nama, alamat, nim,semester,skripsi):
        self.skripsi = skripsi
        super().__init__(nama, alamat,nim,semester)
       
    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nim,self.semester,self.skripsi, self.jabatan)
   
    # @classmethod
    # def matkul(cls,matkul):
    #     cls.matkul = matkul
        
    # @classmethod
    # def ketmatkul(cls):
    #     return 'Mengambil matakuliah {}'.format(cls.matkul)
    

class MahasiswaS2(Mahasiswa):
    jabatan = 'Mahasiswa S2'
    def __init__(self, nama, alamat, nim, semester, tesis,spp):
        self.tesis = tesis
        self.spp = spp
        super().__init__(nama, alamat, nim, semester)

    def __str__(self):
        return '{} | {} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nim, self.semester, self.tesis,self.spp)

class MahasiswaS3(Mahasiswa):
    jabatan = 'Mahasiswa S3'
    def __init__(self, nama, alamat, nim, semester,penelitian):
        self.penelitian = penelitian
        self.gelar = "Doktor"
        super().__init__(nama, alamat, nim, semester)
        
    def __str__(self):
        return '{} | {} | {} | {} | {} | {}'.format(self.nama, self.alamat, self.nim, self.semester, self.penelitian,self.gelar)

    def kampus(self,kuliah):
        self.kuliah = kuliah

    def ketkampus(self):
        return 'Sedang Kuliah di {}'.format(self.kuliah)
    
printmahasiswaS1 = MahasiswaS1('Adi','Magelang','2021075','8','Penerapan')    
print(printmahasiswaS1)
# MahasiswaS1.matkul("Statistika")
# print(MahasiswaS1.ketmatkul())

printmahasiswaS2 = MahasiswaS2('Bayu', 'Banten', '2018071', '4', 'Analisis','6000000')
print(printmahasiswaS2)

printmahasiswaS3 = MahasiswaS3('Joko', 'Tulungagung', '2018071', '5', 'Aplikasi')
print(printmahasiswaS3)
# printmahasiswaS3.kampus("Unsika")
# print(printmahasiswaS3.ketkampus())
