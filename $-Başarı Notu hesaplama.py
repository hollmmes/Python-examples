vize=input("Vize notunuzu giriniz:")
final=input("Final notunuzu giriniz:")

basari=(int(vize)*40/100)+(int(final)*60/100)
if(basari>=60):
    print("Geçtiniz, Tebrikler")
else:
    print("Kaldınız, Üzgünüm ve Bütünlemeye girmek zorundasınız.")
    bütgir1=input("Büt notunuzu giriniz: ") 
    yenibasari1=(int(vize)*40/100)+(int(bütgir1)*60/100)
    if(yenibasari1>=60):
        print("Sonunda geçtiniz tebrikler.")
        exit()
    else:
        print("Bundada kaldın helal olsun")
        exit()
    
bütgir=input("Büte girmek istiyorsanız:E, Girmek istemiyorsanız:H'ye Tıklayınız: ")
if(bütgir=="H"):  
    print("Demek girmeyeceksin he bb o zmn")
elif(bütgir=="E"):
    büt=input("Bütünleme sınavı notunuzu giriniz:")
    yenibasari=(int(vize)*40/100)+(int(büt)*60/100)
    if(yenibasari>=60):
        print("Sonunda geçtiniz tebrikler.")
    else:
        print("Bundada kaldın helal olsun")

