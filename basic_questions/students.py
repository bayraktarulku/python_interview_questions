class OgrenciSinifi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ad, soyad, numara):
        ogrenci = {"ad": ad, "soyad": soyad, "numara": numara}
        self.ogrenciler.append(ogrenci)
        print(f"{ad} {soyad} öğrencisi sınıfa eklendi.")

    def ogrenci_cikar(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci["numara"] == numara:
                self.ogrenciler.remove(ogrenci)
                print(f"{ogrenci['ad']} {ogrenci['soyad']} öğrencisi sınıftan çıkarıldı.")
                return
        print(f"{numara} numaralı öğrenci bulunamadı.")

    def ogrencileri_listele(self):
        print("Sınıftaki öğrenciler:")
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci['ad']} {ogrenci['soyad']} - {ogrenci['numara']}")

    def ogrenci_detay_getir(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci["numara"] == numara:
                print(f"Öğrenci Detayları:\nAd: {ogrenci['ad']}\nSoyad: {ogrenci['soyad']}\nNumara: {ogrenci['numara']}")
                return
        print(f"{numara} numaralı öğrenci bulunamadı.")


# Sınıfı kullanma örneği:
if __name__ == "__main__":
    sinif = OgrenciSinifi()

    while True:
        print("1 - Öğrenci Ekle")
        print("2 - Öğrenci Çıkar")
        print("3 - Öğrenci Listele")
        print("4 - Öğrenci Detayları")
        print("0 - Çıkış")
        secim = input("Seçiminizi yapın (0-4): ")

        if secim == "1":
            ad = input("Öğrencinin adını girin: ")
            soyad = input("Öğrencinin soyadını girin: ")
            numara = input("Öğrencinin numarasını girin: ")
            sinif.ogrenci_ekle(ad, soyad, numara)
        elif secim == "2":
            numara = input("Çıkarmak istediğiniz öğrencinin numarasını girin: ")
            sinif.ogrenci_cikar(numara)
        elif secim == "3":
            sinif.ogrencileri_listele()
        elif secim == "4":
            numara = input("Detaylarını görmek istediğiniz öğrencinin numarasını girin: ")
            sinif.ogrenci_detay_getir(numara)
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
