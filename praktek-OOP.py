#nopal

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.__buku = []

    def tambah_buku(self, buku):
        self.__buku.append(buku)

    def tampilkan_buku(self):
        for buku in self.__buku:
            print(buku.info())

    def __str__(self):
        return f"Perpustakaan: {self.nama}"
class Buku:
    def __init__(self,judul,penulis):
        self.judul = judul
        self.Penulis = penulis

    def info(self):
        return f"Buku: {self.judul} oleh {self.Penulis}"
    
class BukuFiksi(Buku):
    def __init__(self, judul, penulis, genre):
        super().__init__(judul, penulis)
        self.genre = genre

    def info(self):
        return f"Buku Fiksi: {self.judul} oleh {self.Penulis}, Genre: {self.genre}"
    
class BukuNonFiksi(Buku):
    def __init__(self, judul, penulis, topik):
        super().__init__(judul, penulis)
        self.topik = topik

    def info(self):
        return f"Buku Non-Fiksi: {self.judul} oleh {self.Penulis}, Topik: {self.topik}"
    
perpustakaan = Perpustakaan("Perpustakaan kota")

buku1 = BukuFiksi("HarryPotter", "J.K. Rowling", "Fantasi")
buku2 = BukuNonFiksi("sapiens", "yuval noah harari", "sejarah")

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)

print(perpustakaan)
perpustakaan.tampilkan_buku()