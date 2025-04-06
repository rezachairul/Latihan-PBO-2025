# File: 08_Latihan.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: PBO-RC
# ===================================================================================================
# Latihan 1
from abc import ABC, abstractmethod

# Kelas abstrak Kendaraan
class Kendaraan(ABC):
    def __init__(self, warna, harga):
        self.warna = warna
        self.harga = harga
    
    @abstractmethod
    def maju(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass
    
    @abstractmethod
    def ngebut(self):
        pass
    
    def klakson(self):
        print("Beep! Beep!")

# Subclass Mobil
class Mobil(Kendaraan):
    def maju(self):
        print("Mobil bergerak maju.")
    
    def berhenti(self):
        print("Mobil berhenti.")
    
    def ngebut(self):
        print("Mobil melaju dengan kecepatan tinggi!")

# Subclass Truk
class Truk(Kendaraan):
    def maju(self):
        print("Truk bergerak maju.")
    
    def berhenti(self):
        print("Truk berhenti.")
    
    def ngebut(self):
        print("Truk melaju dengan kecepatan tinggi!")

# Subclass SepedaMotor
class SepedaMotor(Kendaraan):
    def maju(self):
        print("Sepeda motor bergerak maju.")
    
    def berhenti(self):
        print("Sepeda motor berhenti.")
    
    def ngebut(self):
        print("Sepeda motor melaju dengan kecepatan tinggi!")

mobil = Mobil("Merah", 200_000_000)
truk = Truk("Biru", 500_000_000)
motor = SepedaMotor("Hitam", 20_000_000)

print("Mobil", mobil.warna, "seharga", mobil.harga, "rupiah.", mobil.maju(), mobil.ngebut(), "sambil membunyikan", mobil.klakson())

# mobil.maju()
# mobil.klakson()
# mobil.ngebut()
# print("=====================================")
# print("Mobil", mobil.warna, "seharga", mobil.harga, "rupiah.", mobil.maju(), mobil.ngebut(), "sambil membunyikan", mobil.klakson())
# print("=====================================")
# truk.maju()
# truk.klakson()
# truk.ngebut()
# print("=====================================")
# print("Truk", truk.warna, "seharga", truk.harga, "rupiah.", truk.maju(), truk.ngebut(), "sambil membunyikan", truk.klakson())
# print("=====================================")
# motor.maju()
# motor.klakson()
# motor.ngebut()
# print("=====================================")
# print("Sepeda motor", motor.warna, "seharga", motor.harga, "rupiah.", motor.maju(), motor.ngebut(), "sambil membunyikan", motor.klakson())
# ===================================================================================================

