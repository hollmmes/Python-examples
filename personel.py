class PersonelOzellikleri:
    gunluk_ucret=250
    personel_list=[]
    
    def __init__(self, isim, soyad, gorev, demirbas, calistigi_gun):
        self.isim = isim
        self.soyad = soyad
        self.gorev = gorev
        self.demirbas = demirbas
        self.calistigi_gun = calistigi_gun
        PersonelOzellikleri.personel_list.append(self) 
    
    
    def ucret_hesapla(self):
        if self.gorev=="CEO":
            return self.calistigi_gun * 500
        elif self.gorev=="CEO Yardımcısı":
            return self.calistigi_gun * 350
        else:
            return self.calistigi_gun * self.gunluk_ucret
        
    @classmethod
    def personel_sil(cls, isim):
        for personel in PersonelOzellikleri.personel_list:
            if personel.isim == isim:
                cls.personel_list.remove(personel)
                break
        
    @classmethod
    def personel_listesi_temizle(cls):
        cls.personel_list.clear()

def kontrol():
    for personel in PersonelOzellikleri.personel_list: 
        ucret = personel.ucret_hesapla() 
        print(personel.isim, personel.soyad, personel.gorev, personel.demirbas, personel.calistigi_gun, ucret)

def parakontrol():
    for personel in PersonelOzellikleri.personel_list:
        ucret = personel.ucret_hesapla() 
        if personel.gorev == "CEO":
            print(personel.isim, personel.soyad,"'nın aldığı",personel.calistigi_gun,"günlük maaş: ",ucret,"(",personel.gorev,"normal maaşa (250TL) göre daha fazla kazanırlar",")")
        elif personel.gorev == "CEO Yardımcısı":
            print(personel.isim, personel.soyad,"'nın aldığı",personel.calistigi_gun,"günlük maaş: ",ucret,"(",personel.gorev,"normal maaşa (250TL) göre daha fazla kazanırlar",")")
        else:
            print(personel.isim, personel.soyad,"'nın aldığı",personel.calistigi_gun,"günlük maaş: ",ucret)
        
def girdi():
    girdidevam=1
    while girdidevam==1:
        girdi= input("Listeden eleman silmek için (Silmek), listeyi kontrol etmek için (Kontrol), Listeyi tamamen temizlemek için (Temizlemek) yazınız.: ").upper()
        if girdi=="SILMEK":
            y=input("Silinmesini istediğiniz kişinin ismini giriniz: ")
            print("-"*25)
            PersonelOzellikleri.personel_sil(y)
            print(kontrol())
            print("-"*25)
            girdidevam=1
        elif girdi == "TEMIZLEMEK":
            print("-Tüm Listeyi temizler-")
            PersonelOzellikleri.personel_listesi_temizle()
            print(PersonelOzellikleri.personel_list) 
            print("-"*25)
            girdidevam=0
        elif girdi=="KONTROL":
            girdidevam=0
            control()
            
def control():
    kontroldevam=1
    while kontroldevam==1:
        girdikontrol = input ("Listeyi Kontrol için (Kontrol), Maaş kontrol için (Maas kontrol), Çıkmak için (Cıkıs), Programı sonlandırmak için (Bitir) Yazınız:  ").upper()
        if girdikontrol =="KONTROL":
            print("-"*25)
            print(kontrol())
            kontroldevam=1
        elif girdikontrol =="MAAS KONTROL":
            print("-"*25)
            print(parakontrol())
            kontroldevam=1
        elif girdikontrol =="CIKIS":
            kontroldevam=0
            girdi()
        elif girdikontrol =="BITIR":
            print("PROGRAM SONLANDI")
            kontroldevam=0

        


        