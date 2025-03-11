# File: 120140086_Reza_Tgs2.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Tugas:
import math
import random

# 1. Kalkulator Sederhana dengan Dunder Methods
class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self):
        if self.value <= 0:
            raise ValueError("Logaritma hanya untuk angka positif!")
        return Calculator(math.log(self.value))

    def __str__(self):
        return str(self.value)

# Contoh penggunaan kalkulator
a = Calculator(10)
b = Calculator(5)

print("Tambah:", (a + b))
print("Kurang:", (a - b))
print("Kali:", (a * b))
print("Bagi:", (a / b))
print("Pangkat:", (a ** b))
print("Log:", (a.log()))


# 2. Simulasi Pewarisan Golongan Darah
class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type  # Contoh: "A", "B", "AB", "O"

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father_allele = random.choice(self.get_alleles(father.blood_type))
        self.mother_allele = random.choice(self.get_alleles(mother.blood_type))
        self.blood_type = self.determine_blood_type()

    def get_alleles(self, blood_type):
        """Mengembalikan alel berdasarkan golongan darah"""
        blood_alleles = {
            "A": ["A", "O"],
            "B": ["B", "O"],
            "AB": ["A", "B"],
            "O": ["O", "O"]
        }
        return blood_alleles[blood_type]

    def determine_blood_type(self):
        """Menentukan golongan darah anak berdasarkan alel dari orang tua"""
        possible_blood_types = {
            ("A", "A"): "A",
            ("A", "O"): "A",
            ("O", "A"): "A",
            ("B", "B"): "B",
            ("B", "O"): "B",
            ("O", "B"): "B",
            ("A", "B"): "AB",
            ("B", "A"): "AB",
            ("O", "O"): "O",
        }
        return possible_blood_types.get((self.father_allele, self.mother_allele), "Unknown")

    def __str__(self):
        return f"Golongan darah anak: {self.blood_type} (Dari alel {self.father_allele} & {self.mother_allele})"

# Contoh penggunaan pewarisan golongan darah
father = Father("A")
mother = Mother("B")
child = Child(father, mother)

print(child)
