mahsulotlar = {
    "non": 5000,
    "olma": 15000,
    "tuxum": 1000,
    "kartoshka": 4000,
}

mahsulot_nomi = input("Mahsulot nomini kiriting: ").lower()

if mahsulot_nomi in mahsulotlar:
    print(mahsulotlar[mahsulot_nomi])
else:
    print("Mahsulot topilmadi")
    
    
talaba = {
    "ism": "Avaz",
    "yosh": 20,
    "kurs": 2
}

talaba["universitet"] = "Termiz davlat universiteti"

print("Barcha kalit va qiymatlar:")
for kalit, qiymat in talaba.items():
    print(kalit, ":", qiymat)