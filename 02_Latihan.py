name = input("Masukkan nama anda: ")
print("Selamat datang," + name + "!")

#Persegi
sisi = int(input("Masukkan panjang sisi persegi: "))
luas = sisi ** 2
volume = sisi ** 3
print("Luas persegi dengan panjang sisi " + str(sisi) + "adalah: " + str(luas) + ".")
print("Volume persegi dengan panjang sisi " + str(sisi) + "adalah: " + str(volume) + ".")

#Persegi Panjang
panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))
luas = panjang * lebar
volume = panjang * lebar * sisi
print("Luas persegi panjang dengan panjang " + str(panjang) + "dan lebar {lebar} adalah: " + str(luas) + ".")
print("Volume persegi panjang dengan panjang " + str(panjang) + "dan lebar {lebar} adalah: " + str(volume) + ".")

#Lingkaran
jari_jari = int(input("Masukkan jari-jari lingkaran: "))
luas = 3.14 * jari_jari ** 2
volume = 4/3 * 3.14 * jari_jari ** 3
print("Luas lingkaran dengan jari-jari " + str(jari_jari) + "adalah: " + str(luas) + ".")
print("Volume lingkaran dengan jari-jari " + str(jari_jari) + "adalah: " + str(volume) + ".")

# Float => Float adalah tipe data yang digunakan untuk menyimpan bilangan desimal.
bilangan = 3.14
print(bilangan) # Output: 3.14
print(type(bilangan)) # Output: <class 'float'>

# String => String adalah tipe data yang digunakan untuk menyimpan teks.
teks = "Belajar Python"
print(teks) # Output: Belajar Python
print(type(teks)) # Output: <class 'str'>

# Boolean => Boolean adalah tipe data yang digunakan untuk menyimpan nilai kebenaran (True, False).
benar = True
salah = False
print(benar) # Output: True
print(type(benar)) # Output: <class 'bool'>
print(salah) # Output: False
print(type(salah)) # Output: <class 'bool'>

#List => List adalah tipe data yang digunakan untuk menyimpan kumpulan data.
buah = ["apel", "jeruk", "mangga"]
print(buah) # Output: ['apel', 'jeruk', 'mangga']
print(type(buah)) # Output: <class 'list'>

#Operasi Logika
# and => Operator logika and akan menghasilkan nilai True apabila kedua operand bernilai True.
# or => Operator logika or akan menghasilkan nilai True apabila salah satu operand bern
# not => Operator logika not akan menghasilkan nilai True apabila operand bernilai False.

#Gaya Penulisan Variabel
# Camel Case => namaVariabel
# Pascal Case => NamaVariabel
# Snake Case => nama_variabel

#Gaya Penulisan Fungsi
# Camel Case => namaFungsi
# Pascal Case => NamaFungsi

#Pengambilan Keputusan
# Percabangan:
#if

#if else
passw = input("Masukan Password anda: ")
if passw == "12345":
    print("Password yang Anda masukkan benar")
else:
    print("Password yang Anda masukkan salah")

#elif


# Perulangan:
# for
passw = input("Mauskan Password anda: ")
for i in range(3):
    if passw == "12345":
        print("Password yang Anda masukkan benar")
    else:
        print("Password yang Anda masukkan salah")

# while
passw = input("Masukan Password anda: ")
while passw != "12345":
    print("Password yang Anda masukkan salah")
    passw = input("Masukan Password anda: ")
print("Password Benar!")
