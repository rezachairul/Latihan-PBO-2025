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

# String Indexing => String Indexing adalah cara untuk mengakses karakter-karakter dalam string.
s = "INFORMATIKA"
print(s[0]) # Output: I
print(s[1]) # Output: N
print(s[2]) # Output: F
print(s[3]) # Output: O
print(s[4]) # Output: R
print(s[5]) # Output: M
print(s[6]) # Output: A
print(s[7]) # Output: T
print(s[8]) # Output: I
print(s[9]) # Output: K
print(s[10]) # Output: A
# String Slicing => String Slicing adalah cara untuk mengambil sebagian string.
s = "INFORMATIKA"
print(s[0:3]) # Output: INF
print(s[0:10]) # Output: INFORMATIKA
print(s[0:11]) # Output: INFORMATIKA
# String Concatenation => String Concatenation adalah cara untuk menggabungkan dua string
s1 = "INFORMATIKA"
s2 = "SEKOLAH"
print(s1 + s2) # Output: INFORMATIKA SEKOLAH

#Operasi String
#1. Uppercase
s = "INFORMATIKA"
print(s.upper()) # Output: INFORMATIKA
#2. Lowercase
s = "INFORMATIKA"
print(s.lower()) # Output: informatika
#3. Title
s = "informatika"
print(s.title()) # Output: Informatika
#4. Capitalize
s = "informatika"
print(s.capitalize()) # Output: Informatika
#5. Panjang Karakter string
s = "INFORMATIKA"
print(len(s)) # Output: 11
#6. Format string sesuai parameter yang diberikan
s = "INFORMATIKA"
print("Saya Kuliah di".format(s, "ITERA")) # Output: INFORMATIKA ITERA

#Fungsi dalam Python
#1. Fungsi Tanpa Parameter
def fungsi_tanpa_paramater():
    print("Fungsi Tanpa Parameter")
    fungsi_tanpa_paramater() # Output: Fungsi Tanpa Parameter
#2. Fungsi Dengan Parameter
def fungsi_dengan_paramater(x):
    print("Fungsi Dengan Parameter")
    print(x)
#3. Fungsi Dengan Parameter dan Return Value
def fungsi_dengan_paramater_dan_return_value(x):
    print("Fungsi Dengan Parameter dan Return Value")
    return x
#4. Fungsi Rekursif
def fungsi_rekursif(x):
    if x == 0:
        return 0
    else:
        return x + fungsi_rekursif(x-1)
#5. Fungsi Faktorial
def faktorial(x):
    if x == 0:
        return 1
    else:
        return x * faktorial(x-1)
#6. Fungsi Lamda
def fungsi_lamda(x):
    return x**2
#7. Fungsi Anonymous
def fungsi_anonim(x):
    return x**2
