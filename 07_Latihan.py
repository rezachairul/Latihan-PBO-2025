# File: 07_Latihan.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: PBO-RC
# ===================================================================================================
# Latihan 1: Grade Tracker Mahasiswa

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = {}

    def add_grade(self, subject, score): # Menambahkan nilai untuk suatu mata kuliah
        if 0 <= score <= 100:
            if subject not in self.__grades: # Jika mata kuliah belum ada di dictionary
                self.__grades[subject] = [] # Membuat list kosong untuk mata kuliah tersebut
            self.__grades[subject].append(score) # Menambahkan nilai ke list mata kuliah tersebut
        else: # Jika nilai tidak valid
            print("Skor harus antara 0 hingga 100!")

    def calculate_average(self, subject=None): # Menghitung rata-rata nilai mahasiswa
        if subject:
            if subject in self.__grades:
                return sum(self.__grades[subject]) / len(self.__grades[subject]) # Menghitung rata-rata nilai
            else:
                print ("Tidak ada data untuk mata kuliah", subject)
                return None
        else: # Menghitung rata-rata nilai
            total_nilai = 0 
            total_jumlah = 0
            for score in self.__grades.values():
                total_nilai += sum(score)
                total_jumlah += len(score)
            return total_nilai / total_jumlah if total_jumlah > 0 else 0
            
        
        

            # total_scores = sum(sum(scores) for scores in self.__grades.values()) # Menghitung total nilai
            # total_count = sum(len(scores) for scores in self.__grades.values()) # Menghitung total jumlah nilai
            # return total_scores / total_count if total_count > 0 else 0 # Menghitung rata-rata nilai

    def get_grades(self): # Mengembalikan nilai mahasiswa
        return self.__grades.copy() # Mengembalikan nilai mahasiswa
    
#  Main Program
student1 = Student("Reza Chairul", "120140086")
student1.add_grade("Pemrograman Berorientasi Objek", 100)
student1.add_grade("Pemrograman Berorientasi Objek", 95)
student1.add_grade("Matematika", 90)
student1.add_grade("Matematika", 80)
student1.add_grade("VisDat", 101)


print("Nilai Pemograman Berorientasi Objek", student1.calculate_average(subject="Pemrograman Berorientasi Objek"))
print("Nilai Matematika", student1.calculate_average(subject="Matematika"))
# print(student1.get_grades(subject="VisDat"))
print("Nilai Visdat", student1.calculate_average(subject="VisDat"))



# Latihan 2: Mobil Listrik VS Mobil Bensin

#Kelas Utama
# class Mobil:


#Sub Kelas Mobil Listrik
# class MobilListrik(Mobil):

#Sub Kelas Mobil Bensin