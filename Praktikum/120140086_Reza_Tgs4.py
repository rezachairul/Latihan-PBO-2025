# File: 120140086_Reza_Tgs4.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Latihan 1:
#abstrak


#polimorfism adalah kemampuan suatu objek untuk merespon berbeda terhadap pemanggilan method yang sama tergantung dari objek yang memanggil method tersebut 

class Mario:
    def action(self):
        print("Mario jumps")
class Sonic:
    def action(self):
        print("Sonic runs")
class Superman:
    def action(self):
        print("Superman flies")

characters = [Mario(), Sonic(), Superman()]
for character in characters:
    character.action() 

# Tugas 1:

#  Method Overloading
# Method overloading adalah kemampuan untuk mendefinisikan beberapa method dengan nama yang sama, tetapi dengan parameter yang berbeda.
# Python tidak mendukung method overloading secara langsung, tetapi kita bisa menggunakan teknik lain untuk mencapainya.
# Salah satu teknik yang bisa digunakan adalah dengan menggunakan default parameter.
#contoh penerapan

