# File: 120140086_Reza_Tgs2.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Latihan:
'''
Buat sebuah program yang menerapkan konsep pewarisan (inheritance) dan enkapsulasi (encapsulation) dengan studi kasus berikut:
Deskripsi Umum
Program ini akan mensimulasikan hirarki kendaraan dengan tiga kelas:
1. Kelas induk Kendaraan (A)
2. Kelas turunan Mobil (B), yang merupakan turunan dari Kendaraan
3. Kelas turunan MobilSport (C), yang merupakan turunan dari Mobil
Pada kelas MobilSport, gunakan konsep enkapsulasi dengan menerapkan getter dan setter untuk propertinya.
'''

class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")
    
    def bergerak(self):
        print("Kendaraan sedang bergerak...")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merek Mobil: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")
    
    def bunyikan_klakson(self):
        print("Beep beep! Mobil membunyikan klakson!")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda  # Private Attribute
        self.__harga = harga  # Private Attribute
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus lebih dari 0!")
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus lebih dari 0!")
    
    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self.__tenaga_kuda} HP")
        print(f"Harga: Rp {self.__harga} juta")
    
    def mode_balap(self):
        print("Mobil Sport masuk ke mode balap!")

# Objek
mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 600, 15000)
mobil_sport.info_mobil_sport()
mobil_sport.mode_balap()

# Getter dan setter
print("Tenaga Kuda sebelum diubah:", mobil_sport.get_tenaga_kuda())
mobil_sport.set_tenaga_kuda(700)
print("Tenaga Kuda setelah diubah:", mobil_sport.get_tenaga_kuda())
print("Harga sebelum diubah:", mobil_sport.get_harga())
mobil_sport.set_harga(16000)
print("Harga setelah diubah:", mobil_sport.get_harga())

#===================================================================================================
# Tugas:
''''
Minggu ini hanya terdiri dari 1 Problem Set. Kalian perlu membuat sebuah permainan sederhana tentang pertarungan Robot.
Kalian akan membuat kelas Robot yang terdiri dari beberapa properti seperti attack, Hp, dll., serta beberapa metode seperti attack_enemy() atau regen_health().
Permainan ini akan berakhir ketika salah satu robot memiliki Hp = 0.
'''
import random

class Robot: # Kelas Robot
    def __init__(self, name, hp, attack_power): 
        self.name = name 
        self.hp = hp 
        self.attack_power = attack_power 
    
    def attack_enemy(self, enemy): # Metode untuk menghancurkan musuh
        if random.random() > 0.2:  # 80% chance to hit
            damage = random.randint(self.attack_power - 2, self.attack_power + 2)
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")
    
    def regen_health(self): # Metode untuk meregenerasi HP
        heal = random.randint(5, 15)
        self.hp += heal
        print(f"{self.name} meregenerasi {heal} HP!")
    
    def is_alive(self): # Metode untuk mengecek apakah robot masih hidup
        return self.hp > 0

class Game: # Kelas Game
    def __init__(self, robot1, robot2): 
        self.robot1 = robot1 
        self.robot2 = robot2 
        self.round = 1
    
    def start(self): # Metode untuk memulai pertarungan
        while self.robot1.is_alive() and self.robot2.is_alive(): # Looping selama kedua robot masih hidup
            print(f"\nRound-{self.round} ==========================================================")
            print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack_power}]")
            print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack_power}]")
            
            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]: # Bergantian menyerang
                if not robot.is_alive() or not enemy.is_alive(): # Jika salah satu robot sudah mati,
                    break
                action = input(f"{robot.name}, pilih aksi: 1. Attack 2. Regen 3. Giveup\n") # Pilihan aksi
                if action == "1":
                    robot.attack_enemy(enemy)
                elif action == "2":
                    robot.regen_health()
                elif action == "3":
                    print(f"{robot.name} menyerah! {enemy.name} menang!")
                    return
            self.round += 1
        
        winner = self.robot1 if self.robot1.is_alive() else self.robot2 # Menentukan pemenang
        print(f"\n{winner.name} menang!")

# Objek Robot
robot1 = Robot("Zhask", 500, 10)
robot2 = Robot("Jhonson", 750, 8)

battle = Game(robot1, robot2) # Objek Game
battle.start() # Memulai pertarungan
