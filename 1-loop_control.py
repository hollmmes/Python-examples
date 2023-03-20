
while True:
    name = input("ismini gir: ")
    if name != "":
        break  # döngülerden tamamen çıkmak için değer girilirse çıkmasını söyleidk
print("teşekkürler "+name)   

phone_num= "0123-456-789"
for i in phone_num:
    if i == "-":
        continue   # - gördüğünde sil ve yazmaya devam et komutu
    print(i, end="")
    
print(" ")
for i in range(1,7):
    if i == 4: # 4ü yazdırmadan diğerlerini yazdırdık
        pass
    else:
        print(i)
