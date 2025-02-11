class JusBuah:
    def __init__(self, nama_buah, gula):
        # Enkapsulasi
        self.nama_buah = nama_buah #Protected
        self.gula = gula #Private

    def buat_jus(self):
        print(f"Membuat jus {self.nama_buah} dengan {self.gula} gram gula.")

# Pewarisan
class JusJeruk(JusBuah):
    def __init__(self, gula):
        super().__init__("Jeruk", gula)

class JusApel(JusBuah):
    def __init__(self, gula):
        super().__init__("Apel", gula)

# Polimorfisme
def sajikan_jus(jus):
    jus.buat_jus()

if __name__ == "__main__":
    jus_jeruk = JusJeruk(10)
    jus_apel = JusApel(5)
    # Hasil
    sajikan_jus(jus_jeruk)
    sajikan_jus(jus_apel)