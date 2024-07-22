"""sicaklik = int(input("Fahrenheit Değeri Giriniz : "))
santigrat = (sicaklik - 32) * 5/9
print("C değeri :" , santigrat)"""

"""sicaklik = int(input("Fahrenheit Değeri Giriniz : "))
fahr = (sicaklik * 9/5) +32
print("C değeri :" , fahr)"""

"""taban = int(input("Taban Uzunluğunu Girniz : "))
yukseklik = int(intput("Yukseklik : "))
alan = taban * yukseklik / 2
print("Alan : ", alan)"""

"""vize = int(input("Vize Notunuz : "))
final = int(input("Final Notunuz : "))

GECMENOTU = 70

notu = vize * 0.3 + final * 0.7

if notu >= GECMENOTU:
    print("GEÇTI")
else:
    print("ÇAKTI")"""



"""maas = int(input("Maas Giriniz : "))
cocuk = int(input("Cocuk Sayısı : "))
if cocuk == 1:
    maas *= 1.05
elif cocuk == 2:
    maas *= 1.1
elif cocuk >=3:
    maas*= 1.15
else:
    maas = maas
print("Alacağınız Maas : ", maas) """


"""isim = (input("Bacım adını gir : "))

sayac = 1
while sayac < 11:
    sayac += 1
    print(isim)"""



"""sayi = int(input("Sayi gir :"))

tekSayiToplam = 0
tekSayiCarp = 1
ciftSayiTop = 0

sayac = 1

while sayac <=sayi:
    sayac+=1
    if sayac % 2 == 0 :
        ciftSayiTop+= sayac**2
    else:
        tekSayiCarp *=sayac
        tekSayiToplam += sayac
    
print(tekSayiCarp, tekSayiToplam, ciftSayiTop)
"""

"""sayac = 1
sayi = int(input("Sayı gir : "))
top = 0
while sayac <= sayi:
    sayac+=1
    top +=sayac
print(top)"""




"""yas = 75
print(f"Girdiğiniz sayi {yas} dir")

isim = "Rahime"
soyisim = "Aydan"

tumIsim = isim + soyisim
print(isim + soyisim)
print(tumIsim)
print(isim + str(yas) + "yasında")"""


#print(5*"+-+")

"""print("+" + 10 * "-" + "+")
print("+" + 10 * " " + "+")
print("+" + 10 * "-" + "+")

isim = "Deniz CANTÜRK"
print(len(isim))"""

isim = "Deniz"
uz = len(isim)

charSayisi = uz + 10
print("+" + charSayisi*"-" + "+")

print("+" + ((charSayisi-uz)//2) * " " + isim  + ((charSayisi-uz)//2) * " " + "+")

print("+" + charSayisi*"-" + "+")
