class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = {}

    def tambah_nilai(self, mata_kuliah, nilai):
        """Menambahkan nilai mata kuliah ke dalam daftar nilai"""
        self.nilai[mata_kuliah] = nilai

    def hitung_rata_rata(self):
        """Menghitung rata-rata nilai mahasiswa"""
        if not self.nilai:
            return 0
        return sum(self.nilai.values()) / len(self.nilai)

    def tampilkan_info(self):
        """Menampilkan informasi mahasiswa"""
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.prodi}")
        print("Daftar Nilai:")
        for mk, nilai in self.nilai.items():
            print(f"  - {mk}: {nilai}")
        print(f"Rata-rata Nilai: {self.hitung_rata_rata():.2f}")


# Logika Main
if __name__ == "__main__":
    mhs1 = Mahasiswa("Reza Chairul Manam", "120140086", "Teknik Informatika")
    
    mhs1.tambah_nilai("Algoritma", 85)
    mhs1.tambah_nilai("Struktur Data", 90)
    mhs1.tambah_nilai("Basis Data", 88)

    mhs1.tampilkan_info()
