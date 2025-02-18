#Review Latihan Mg 2
# def balik_string(kata):
#     return kata[::-1]
# kata_dibalik = input("Masukkan string: ")
# print("Hasil balik:", balik_string(kata_dibalik))

# # Ambil 3 karakter didepan
# def ambil_3_karakter(kata):
#     return kata[:3]
# kata_dipilih = input("Masukkan string: ")
# print("Hasil ambil 3 karakter:", ambil_3_karakter(kata_dipilih))

# ====================================================================#
# Latihan Mg 3
#  List
data_siswa =["Ahmad", 17, False]
# Operasi pada List
daftar_kegiatan = ["Ngaji", "makan", "main", "tidur"]
print ('belajar' in daftar_kegiatan) # True
#Append
daftar_kegiatan.append("belajar")
# del daftar_kegiatan[3] # Hapus index ke 3
print(daftar_kegiatan) # ['Ngaji', 'makan', 'main', 'tidur ', 'belajar']
#iterasi list
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for i in range(len(data)):
    print(data[i])
for i in range(0, len(data), 2):
    print(data[i])

#index list
siswa_kegiatan = ["belajar", "makan", "main", "tidur"]
    #reverse
siswa_kegiatan.sort()
print(siswa_kegiatan)

#tipe data Tupel
# Tidak dapat diubah
# Tidak dapat dihapus
# Tidak dapat ditambahkan
# Tidak dapat diurutkan
# Tidak dapat diubah urutannya
# Tidak dapat diubah indexnya
# Tidak dapat diubah nilainya
tupel_data1 = (1, 2, 3, 4, 5)
tupel_data2 = 6, 7, 8, 9, 10
tupel_data3 = tuple("ABCDEFGHIJ")
print(tupel_data1, tupel_data2,tupel_data3)
