import math

print("*" * 31)
print("Açı\tSin\tCos\tTan")                 # tablo görünümü için tab boşluğu bıraktım
print("*" * 31)

for i in range(0, 181, 1):                  # 180 yaptım çünkü her sayının yarısını alacak bu da 0dan90a kadar oluyor 
    acı = i/2 
    radyan = math.radians(acı)              #https://www.w3schools.com/python/ref_math_radians.asp burada örnek aldım
    sin= round(math.sin(radyan), 4)
    cos = round(math.cos(radyan), 4)
    if acı == 90 :                          # tanjant 90 tanımsızdır onun için özel bir if else ayarladım
        tan = "tan(90) tanımsızdır"
    else:
        tan = round(math.tan(radyan), 4) 
    print(f"{acı}\t{sin}\t{cos}\t{tan}")    # ilk baştaki tablo görüntüsüne uygun yapmak için /t kullandım ki alt alta gelsinler
    print("-" * 31)
