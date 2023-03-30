# çağrıldığı zaman çalışan kodlar

def main(name):             #fonksiyonun kendi
    print("Hello! "+name+"!")

main("Tufi") # fonskiyonu çağırma yeri
main("Aleynay"),main("Allah")

print(" ")

def main(name,surname):             #fonksiyonun kendi
    print("Hello! "+name+" "+surname+"!")

main("Tufi","hm") # fonskiyonu çağırma yeri
main("Aleynay","mh"),main("Allah","yokbu")

print(" ")

def mult(number1,number2):
    res=number1+number2
    return res


x=input("gir: ")
y=input("gir2: ")
print(mult(x,y))
