class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = []

    def not_ekle(self, ders, not_degeri):
        self.notlar.append({"ders": ders, "not": not_degeri})
        print(f"{self.ad} adlı öğrencinin {ders} dersi notu eklendi.")

    def notlarini_goster(self):
        print(f"{self.ad} {self.soyad} Notları:")
        for not_bilgisi in self.notlar:
            print(f"{not_bilgisi['ders']}: {not_bilgisi['not']}")


ogrenci = Ogrenci(input("Adınız: "), input("Soyadınız: "), input("Numaranız: "))

while True:
    print("Not eklemek için 1'e basın")
    print("Notlarınızı görmek için 2'ye basın")
    print("Çıkış için 3'ya basın")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ders = input("Ders adını girin: ")
        not_degeri = input("Not değerini girin: ")
        ogrenci.not_ekle(ders, not_degeri)
    elif secim == "2":
        ogrenci.notlarini_goster()
    elif secim  == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
