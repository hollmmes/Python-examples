
a=1
while a==1:
    mail = str(input("E-mail adresinizi giriniz: "))            # xxxxxx@eposta.com
    hmm1= mail.endswith("@eposta.com")                           #eposta.com ile mi bitiyor 
    if hmm1 == True:
        if mail == "@eposta.com":
            print("E-mail adresinizi doğru bir şekilde giriniz")
        else:
            print("E-mail adresiniz doğrulandı")
            a=2
    else:
        print("E-mail adresinizi doğru bir şekilde giriniz")
