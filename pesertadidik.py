class Mahasiswa:
    def __init__(self, nama, alamat, nim,semester):
        self.nama = nama
        self.alamat = alamat
        self.nim = nim
        self.semester = semester

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.nama, self.alamat, self.nim,self.semester)


if __name__ == '__main__':
    printmahasiswa = Mahasiswa('Fauzan', 'Jakarta', '171000063131',8)
    print(printmahasiswa)
