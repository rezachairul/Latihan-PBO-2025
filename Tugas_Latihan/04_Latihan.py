# #Kelas dan Objek dalam python
# class Mobil:
#     jumlah_mobil = 0
#     # init atribute
#     def __init__(self, nama, warna, merek, jumlah_mobil): # fungsi yang dipanggil saat objek dibuat
#         self.nama = nama
#         self.warna = warna
#         self.merek = merek
#         Mobil.jumlah_mobil += 1
    
#     def __str__(self): #method untuk merepresentasikan objek sebagai string
#         return f"Nama Mobil: {self.nama}, Warna: {self.warna}, Merek: {self.merek}"
#     def maju (self):
#         print ("Mobil " + self.nama + " sedang Maju")
#     def mundur (self):
#         print ("Mobil " + self.nama + " sedang mundur")

# print("jumlah mobil sebelum membuat objek:", Mobil.jumlah_mobil)
# # Membuat objek mobil
# mobil1 = Mobil("Toyota", "Merah", "Ayla", 0)
# mobil2 = Mobil("Honda", "Biru", "Civic", 0)

# mobil1.maju()
# mobil1.mundur()

# print("jumlah mobil setelah membuat objek:", Mobil.jumlah_mobil)

#==============================================================================
# Latihan Kelas Sepeda
# Setiap sepeda memiliki 4 roda gigi
# • Jika posisi roda gigi 1 maka max_kecepatan = 2, roda
# gigi 2 maka max_kecepatan = 4, roda gigi 3 maka
# max_kecepatan = 6, dan roda gigi 4 maka
# max_kecepatan = 8.
# Kecepatan boleh nol dan tidak boleh lebih besar dari
# max_kecepatan

class Sepeda:
    def __init__(self):
        self.roda_gigi_saat_ini = 1
        self.max_kecepatan = 2
        self.kecepatan = 0

    def pindah_roda_gigi(self, roda_gigi):
        if 1 <= roda_gigi <= 4:
            self.roda_gigi_saat_ini = roda_gigi
            self.max_kecepatan = roda_gigi * 2  

            if self.kecepatan > self.max_kecepatan:
                self.kecepatan = self.max_kecepatan

            print(f"\n✅ Roda gigi berpindah ke {roda_gigi}")
        else:
            print("\n⚠️ Roda gigi harus antara 1 hingga 4")

        self.tampilkan_status()

    def menambah_kecepatan(self):
        if self.kecepatan < self.max_kecepatan:
            self.kecepatan += 1
            print("\n✅ Kecepatan bertambah")
        else:
            print("\n⚠️ Kecepatan sudah maksimum!")

        self.tampilkan_status()

    def menurunkan_kecepatan(self):
        if self.kecepatan > 0:
            self.kecepatan -= 1
            print("\n✅ Kecepatan berkurang")
        else:
            print("\n⚠️ Kecepatan sudah 0!")

        self.tampilkan_status()

    def tampilkan_status(self):
        print(f"🚴‍♂️ Kecepatan: {self.kecepatan} | ⚙️ Roda Gigi: {self.roda_gigi_saat_ini} | 🔺 Max Kecepatan: {self.max_kecepatan}\n")

# Membuat objek sepeda
sepeda1 = Sepeda()

while True:
    print("\n🚴‍♂️ === Menu Sepeda ===")
    print("1. Pindah Roda Gigi")
    print("2. Menambah Kecepatan")
    print("3. Menurunkan Kecepatan")
    print("4. Tampilkan Status")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        try:
            roda_gigi = int(input("Masukkan roda gigi (1-4): "))
            sepeda1.pindah_roda_gigi(roda_gigi)
        except ValueError:
            print("\n⚠️ Masukkan angka yang valid!")

    elif pilihan == "2":
        sepeda1.menambah_kecepatan()

    elif pilihan == "3":
        sepeda1.menurunkan_kecepatan()

    elif pilihan == "4":
        sepeda1.tampilkan_status()

    elif pilihan == "5":
        print("\n🚴 Program selesai. Terima kasih!")
        break

    else:
        print("\n⚠️ Pilihan tidak tersedia, coba lagi!")
