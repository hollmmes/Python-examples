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
        print("Hoş Geldiniz")
        a=2
    else:  
        print("Hatalı giriş yaptınız")


