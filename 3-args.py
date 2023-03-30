# tuplea girebilecek tüm değerler işte bu 
# önemli olan args ifadesinin önüdeki yıldız (*) işaretidir!!

def add(*args):
    print(*args)
    args = list(args) #tuple olan argsi liste args a çevirdik ki içeriyi kontrol edebilelim
    args[0]=10 #içeiriyi değiştirdik
    print(*args)
    sum = 0
    for i in args:
        sum+= i
    return sum

print(add(1,2,3,4,5,6,7)) # gönderilen değerler aslında tuple = (1,2,3) olarak gitti ve her biri işleme girdi

