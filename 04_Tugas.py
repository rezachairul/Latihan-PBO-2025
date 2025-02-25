class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = {}  # Menyimpan nilai mata kuliah sebagai dictionary

    def tambah_nilai(self, mata_kuliah, nilai):
        # Menambahkan nilai untuk suatu mata kuliah
        self.nilai[mata_kuliah] = nilai

    def hitung_rata_rata(self):
        # Menghitung rata-rata nilai mahasiswa
        if len(self.nilai) == 0:
            return 0
        total = sum(self.nilai.values())
        return total / len(self.nilai)

    def tampilkan_info(self):
        # Menampilkan informasi mahasiswa
        print("Nama         :", self.nama)
        print("NIM          :", self.nim)
        print("Program Studi:", self.prodi)
        print("Nilai:")
        for mk, nilai in self.nilai.items():
            print("  -", mk, ":", nilai)
        print("Rata-rata    :", self.hitung_rata_rata())

# Logika main untuk mengakses kelas 
if __name__ == "__main__":
    # Membuat objek mahasiswa dengan data awal
    mhs1 = Mahasiswa("Reza Chairul Manam", "120140086", "Teknik Informatika")
    
    # Menambahkan nilai mahasiswa
    mhs1.tambah_nilai("Object-Oriented Programming", 100)
    mhs1.tambah_nilai("Tugas Akhir-1", 99)
    mhs1.tambah_nilai("Tugas Akhir-2", 99)

    # Menampilkan informasi mahasiswa tersebut
    mhs1.tampilkan_info()
