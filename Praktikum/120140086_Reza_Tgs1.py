# File: 120140086_Reza_Tgs1.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Tugas:
# 1. Buatlah sebuah program yang dapat menampilkan segitiga tergantung dengan tinggi yang ditentukan oleh pengguna.
def segitiga_tergantung(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

# Input height dari user
height = int(input("Masukkan tinggi segitiga: "))
segitiga_tergantung(height)

# 2. Buatlah sebuah program untuk mengisi dictionary dengan data siswa.
# Input jumlah siswa
n = int(input("Masukkan jumlah siswa: "))
siswa = {}

total = 1
for i in range(n):
    nama = input(f"Nama siswa ke-{total}: ")
    nilai = int(input(f"Nilai siswa ke-{total}: "))
    siswa[nama] = nilai
    total += 1
# Output dictionary siswa
print("\nDictionary:", siswa)

# 3. Program untuk membuat file "Me.txt" dan menuliskan data ke dalamnya
# Input dari user
nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
resolusi = input("Masukkan resolusi di tahun ini: ")

# Membuat file "Me.txt" dan menuliskan data ke dalamnya
with open("Me.txt", "w") as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi: {resolusi}\n")
print("\nFile Me.txt berhasil dibuat!")