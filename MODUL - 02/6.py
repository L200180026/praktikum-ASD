class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2
class SiswaSMA(Manusia):
    jurusan = "Belum Ditentukan"
    univ = "Belum Ditentukan"
    def __init__(self, nama, nisn, sma):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
    def __str__(self):
        return "\n\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nUniv Pilihan : "+self.univ\
               +"\nJurusan Pilihan : "+self.jurusan
    def ambil(self):
        print("\n\nUpdate Data Universitas Pilihan...")
        self.univ = input("Pilih Univ : ")
        self.jurusan = input("Ambil Jurusan : ")
