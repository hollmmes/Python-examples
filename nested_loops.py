#iç içe döngüler
            


rows = int(input("kaç sıra istersin? " ))
columns = int(input("kaç sütun istersin? " ))
symbol = input("hangi sembolü istersin? " )

for i in range(rows):
    for j in range(columns):             # iç içe kullanılan iki for döngüsü kullanıldı
        print(symbol, end="")
    print()
