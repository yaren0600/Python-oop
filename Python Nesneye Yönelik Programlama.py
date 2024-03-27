class Personel:
    def __init__(self, adi, departman, calisma_yili, maas):
        self.adi = adi
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.adi)
            print("Departmanı:", personel.departman)
            print("Çalışma Yılı:", personel.calisma_yili)
            print("Maaşı:", personel.maas)
            print("---------------------")

    def maas_zammi(self, personel, zam_orani):
        personel.maas *= (1 + zam_orani / 100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)

# Firma ve personel bilgilerini kullanıcıdan alalım
firma = Firma()

while True:
    adi = input("Personelin adını girin (Çıkmak için 'q' ya basın): ")
    if adi.lower() == 'q':
        break
    departman = input("Personelin departmanını girin: ")
    calisma_yili = int(input("Personelin çalışma yılını girin: "))
    maas = float(input("Personelin maaşını girin: "))

    personel = Personel(adi, departman, calisma_yili, maas)
    firma.personel_ekle(personel)

# Personel bilgilerini listeleme
print("Personel Bilgileri:")
firma.personel_listele()

# Maaş zamı uygulama
while True:
    secim = input("Maaş zammı yapmak istediğiniz personelin adını girin (Çıkmak için 'q' ya basın): ")
    if secim.lower() == 'q':
        break
    for personel in firma.personel_listesi:
        if personel.adi == secim:
            zam_orani = float(input(f"{personel.adi}'nin zam oranını girin (% cinsinden): "))
            firma.maas_zammi(personel, zam_orani)
            break
    else:
        print("Girdiğiniz isimde bir personel bulunamadı!")

print("Maaşları Güncellenmiş Personel Bilgileri:")
firma.personel_listele()

# Bir personeli çıkarma
while True:
    secim = input("Çıkartmak istediğiniz personelin adını girin (Çıkmak için 'q' ya basın): ")
    if secim.lower() == 'q':
        break
    for personel in firma.personel_listesi:
        if personel.adi == secim:
            firma.personel_cikart(personel)
            break
    else:
        print("Girdiğiniz isimde bir personel bulunamadı!")

print("Personel Çıkartıldıktan Sonraki Bilgiler:")
firma.personel_listele()
