# parametreleri dictionaryye çevirir 
# değişken parametre yollarken çok işe yarar

def func(**kwargs):
    for key,val in kwargs.items():
        print(val)
        
func(Ali=12,Mehmet=13,Ayşe=14)


print("-"*50)

def examp(**kwargs):
    for k in kwargs:
        print(k,kwargs[k])
        
examp(ad="Tufancan",soyad="Demirkılıç",yas="20")

print("-"*50)

def toplama(*args, **kwargs): # parameterler keysiz gittiyse args, keyli gittiyse kwargs olurlar yani tuple ve dictionary
    print(args)
    toplam = sum(args)
    print(toplam)
    print(kwargs)
    for i in kwargs:
        print(i,":",kwargs[i])

toplam1=toplama(1,3,5,4,2,6,8,7,9,10,11,12,13,14,15,ad="Tufancan",soyad="Dem")

