# File: 120140086_Reza_Tgs3.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Tugas 1:
import math

class Kalkulator: # Kelas Kalkulator
    def __init__(self, nilai): 
        self.nilai = nilai
    
    def __add__(self, other): # Method untuk menambahkan nilai
        return Kalkulator(self.nilai + other.nilai)
    
    def __sub__(self, other): # Method untuk mengurangkan nilai
        return Kalkulator(self.nilai - other.nilai)
    
    def __mul__(self, other): # Method untuk mengalikan nilai
        return Kalkulator(self.nilai * other.nilai)
    
    def __truediv__(self, other): # Method untuk membagi nilai
        if other.nilai == 0:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan!")
        return Kalkulator(self.nilai / other.nilai)
    
    def __pow__(self, other): # Method untuk menghitung nilai pangkat
        return Kalkulator(self.nilai ** other.nilai)
    
    def log(self, base=10): # Method untuk menghitung nilai logaritma
        if self.nilai <= 0:
            raise ValueError("Logaritma hanya bisa diterapkan pada bilangan positif!")
        return Kalkulator(math.log(self.nilai, base))
    
    def __str__(self): # Method untuk mengubah nilai menjadi string
        return str(self.nilai)

# Program Utama
while True: # Perulangan untuk menghitung kalkulator
    try: 
        angka1 = Kalkulator(float(input("Masukkan angka pertama: "))) # Input angka pertama
        operator = input("Masukkan operator (+, -, *, /, ^, log): ") # Input operator
        if operator == "log": # Jika operator adalah log
            hasil = angka1.log() # Menghitung logaritma
        else: # Jika operator adalah operator matematika
            angka2 = Kalkulator(float(input("Masukkan angka kedua: ")))
            if operator == "+": 
                hasil = angka1 + angka2
            elif operator == "-":
                hasil = angka1 - angka2
            elif operator == "*":
                hasil = angka1 * angka2
            elif operator == "/":
                hasil = angka1 / angka2
            elif operator == "^":
                hasil = angka1 ** angka2
            else:
                print("Operator tidak valid!")
                continue
        
        print(f"Hasil: {hasil}") # Output hasil
    except ValueError as e:
        print(f"Error: {e}") # Output error
    
    lanjut = input("Ingin menghitung lagi? (y/n): ") # Input untuk mengulang program
    if lanjut.lower() != "y":
        break # Keluar dari perulangan jika input tidak y

#===================================================================================================
# Tugas 2:
import random # Import modul random

class Father: # Kelas Father
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother: # Kelas Mother
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child: # Kelas Child
    def __init__(self, father, mother): 
        self.father_blood = father.blood_type 
        self.mother_blood = mother.blood_type 
        self.blood_type = self.determine_blood_type() # Memanggil method determine_blood_type
    
    def determine_blood_type(self): # Method untuk menentukan golongan darah anak
        blood_map = { # Dictionary untuk menentukan golongan darah anak
            ('A', 'A'): 'A', ('A', 'B'): 'AB', ('A', 'O'): 'A', ('A', 'AB'): random.choice(['A', 'AB']), 
            ('B', 'B'): 'B', ('B', 'O'): 'B', ('B', 'AB'): random.choice(['B', 'AB']), 
            ('O', 'O'): 'O', ('O', 'AB'): random.choice(['A', 'B']),
            ('AB', 'AB'): random.choice(['A', 'B', 'AB'])
        }
        
        alel_father = random.choice(self.father_blood) # Memilih alel golongan darah ayah
        alel_mother = random.choice(self.mother_blood) # Memilih alel golongan darah ibu
        return blood_map.get((alel_father, alel_mother), blood_map.get((alel_mother, alel_father))) # Menentukan golongan darah anak berdasarkan alel ayah dan ibu
    
    def display_info(self): # Method untuk menampilkan informasi golongan darah
        print(f"Golongan darah ayah: {self.father_blood}") 
        print(f"Golongan darah ibu: {self.mother_blood}")
        print(f"Golongan darah anak: {self.blood_type}")

# Input dari pengguna
father_blood = input("Masukkan golongan darah ayah (A, B, O, AB): ").strip().upper() # Input golongan darah ayah
mother_blood = input("Masukkan golongan darah ibu (A, B, O, AB): ").strip().upper() # Input golongan darah ibu

father = Father(father_blood) # Objek Father
mother = Mother(mother_blood) # Objek Mother
child = Child(father, mother) # Objek Child

child.display_info() # Output informasi golongan darah anak