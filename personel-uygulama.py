from personel import PersonelOzellikleri,kontrol,parakontrol,girdi,control
tekrar=0
while tekrar==0:
    try:
        personel1 = PersonelOzellikleri("Aleyna", "Yargeldi", "CEO", ["MAC", "İphone"], int(input("Aleyna'nın çalıştığı günü giriniz: ")))
        personel2 = PersonelOzellikleri("Tufancan", "Demirkılıç", "CEO Yardımcısı", ["Bilgisayar", "Telefon"], int(input("Tufancan'nın çalıştığı günü giriniz: ")))
        personel3 = PersonelOzellikleri("Hakan","Arslan","Kaptan",["Gemi"], int(input("Hakan'ın çalıştığı günü giriniz: ")))
        personel4 = PersonelOzellikleri("Kemal","Çamcı","Camcı",["Cam"],int(input("Kemal'in çalıştığı günü giriniz: ")))
        personel5 = PersonelOzellikleri("Arif","Teles","Aristoteles'in yeğeni",["Kitap"],int(input("Arif'in çalıştığı günü giriniz: ")))
        
    except ValueError as e:
        print("Gün Boş geçilemez!")
        tekrar=0
    else:
        tekrar=1
    
girdi()

