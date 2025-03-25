# File: 120140086_Reza_Tgs4.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Tugas 1:
import math

class SquareRootCalculator:
    def __init__(self):
        pass

    def get_input(self):
        while True:
            try:
                user_input = input("Masukkan angka: ")
                number = float(user_input)
                if number < 0:
                    print("Input tidak valid. Harap masukkan angka positif.")
                    continue
                elif number == 0:
                    print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
                    continue
                return number
            except ValueError:
                print("Input tidak valid. Harap masukkan angka yang valid.")

    def calculate_square_root(self, number):
        return math.sqrt(number)

    def run(self):
        number = self.get_input()
        result = self.calculate_square_root(number)
        print(f"Akar kuadrat dari {number} adalah {result}")

if __name__ == "__main__":
    calculator = SquareRootCalculator()
    calculator.run()

# Tugas 2:
class ToDoList:
    def __init__(self):
        self.tasks = []

    def tambah_tugas(self):
        tugas = input("Masukkan tugas: ").strip()
        if tugas:
            self.tasks.append(tugas)
            print("Tugas berhasil ditambahkan!\n")
        else:
            print("Error: Tugas tidak boleh kosong.\n")

    def hapus_tugas(self):
        if not self.tasks:
            print("Daftar tugas kosong.\n")
            return
        self.tampilkan_tugas()
        try:
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                print("Tugas berhasil dihapus!\n")
            else:
                print("Error: Nomor tugas tidak valid.\n")
        except ValueError:
            print("Error: Masukkan angka yang valid.\n")

    def tampilkan_tugas(self):
        if not self.tasks:
            print("Daftar tugas kosong.\n")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.tasks, 1):
                print(f"{i}. {tugas}")
            print()

    def jalankan(self):
        while True:
            print("1. Tambah tugas\n2. Hapus tugas\n3. Tampilkan tugas\n4. Keluar")
            pilihan = input("Pilih aksi (1/2/3/4): ")
            if pilihan == "1":
                self.tambah_tugas()
            elif pilihan == "2":
                self.hapus_tugas()
            elif pilihan == "3":
                self.tampilkan_tugas()
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                print("Error: Pilihan tidak valid.\n")

if __name__ == "__main__":
    to_do = ToDoList()
    to_do.jalankan()

# Tugas 3
from abc import ABC, abstractmethod 

class Animal(ABC): 
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string yang valid.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        
        self.__name = name
        self.__age = age
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string yang valid.")
        self.__name = name
    
    def set_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        self.__age = age

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

class Monkey(Animal):
    def make_sound(self):
        return "Ooh ooh aah aah!"

def main(): 
    zoo = []
    while True:
        print("\n1. Tambah Hewan\n2. Tampilkan Hewan\n3. Keluar")
        choice = input("Pilih aksi (1/2/3): ")
        
        if choice == "1":
            print("Pilih jenis hewan: 1. Singa, 2. Gajah, 3. Monyet")
            animal_type = input("Masukkan pilihan (1/2/3): ")
            name = input("Masukkan nama hewan: ")
            try:
                age = int(input("Masukkan usia hewan: "))
                if animal_type == "1":
                    zoo.append(Lion(name, age))
                elif animal_type == "2":
                    zoo.append(Elephant(name, age))
                elif animal_type == "3":
                    zoo.append(Monkey(name, age))
                else:
                    print("Pilihan tidak valid.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            if not zoo:
                print("Belum ada hewan di kebun binatang.")
            else:
                print("Daftar Hewan di Kebun Binatang:")
                for animal in zoo:
                    print(f"{animal.get_name()} ({animal.get_age()} tahun) - Suara: {animal.make_sound()}")
        
        elif choice == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__": 
    main()

