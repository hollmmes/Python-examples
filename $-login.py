sifre="123456"
kullanici_adi="tufi"
a=1
while a==1:
    nick=input("kullanı adı gir: ")
    passw=input("şifre gir: ")
    if(nick!=kullanici_adi):
        print("kullancı adınız yanlış")
    else:
        if(passw!=sifre):
            print("şifreniz yanlış")
    if(nick==kullanici_adi and passw==sifre):
        print("Hoş Geldin Admin")
        a=2
    else:  
        print("Hatalı giriş yaptınız")
data={}
while True:
    id_no= input("Çalışan no: ")
    if not id_no:
        break
    name= input("Çalışan adı:")
    surname = input("Çalışan soyad: ")
    income = int(input("Çalışan maaş: "))
    data.update({ 
        id_no: {
            "ad": name,
            "soyad": surname, 
            "maaş": income,
        }
    })
print("-"*50)
print(data, sep="\n")
print("-"*50)
while True:
    id_gir= input("zam yapılacak çalışanın numarasını giriniz: ")
    if not id_gir:
        break
    if id_gir in data:
        mevcut_maas= data[id_gir]["maaş"]
        print(f"{id_no}numaralı kişinin şu anki maaşı:  {mevcut_maas}")
        zam_orani= float(input("%'kaç zam yapılmasını istersiniz: "))
        yeni_maas=mevcut_maas+mevcut_maas*(zam_orani/100)
        data[id_gir]["maaş"]= yeni_maas
        print(f"{id_gir} numaralı kişini yeni maaşı: {yeni_maas}")
    else:
        print("Geçerli id girmediniz")
print("-"*50)        
print(data, sep="\n")
print("-"*50)




