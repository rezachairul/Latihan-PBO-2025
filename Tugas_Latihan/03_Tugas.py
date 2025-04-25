# List hasil voting
daftar_suara = [
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    "enrinal", "huda", "ivena", "enrinal", "huda", "ivena", "huda", "enrinal", "ivena", "huda", 
    ]

hitung_suara = {}

for nama in daftar_suara:
    if nama in hitung_suara:
        hitung_suara[nama] += 1
    else:
        hitung_suara[nama] = 1

maks_suara = max(hitung_suara.values())

pemenang = []
for nama, suara in hitung_suara.items():
    if suara == maks_suara:
        pemenang.append(nama)

pemenang.sort()

print("Pemenang:", pemenang[0])
print("Total Suara:", maks_suara)
