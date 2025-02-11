#Latihan 1
def pisah(numbers):
    satu_digit = []
    dua_digit = []    
    while numbers:
        number = numbers.pop()
        if number < 10:
            satu_digit.append(number) #append adalah untuk menambahkan nilai ke list
        else:
            dua_digit.append(number) #append adalah untuk menambahkan nilai ke list
    return satu_digit, dua_digit
numbers = [12, 37, 5, 42, 8, 3]
satu_digit, dua_digit = pisah(numbers.copy())

print("Bilangan satu digit:", satu_digit)
print("Bilangan dua digit:", dua_digit)

#Latihan 2
def balik_string(kata):
    return kata[::-1]
kata_dibalik = input("Masukkan string: ")
print("Hasil balik:", balik_string(kata_dibalik))

#Latihan 3
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
bilangan = int(input("Masukkan bilangan bulat positif: "))
if bilangan < 0:
    print("Bilangan harus positif!")
else:
    print(f"Faktorial dari {bilangan} adalah {faktorial(bilangan)}")
