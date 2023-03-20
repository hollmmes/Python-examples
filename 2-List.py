Numaralar = [1,20,12,123,58,3,9]
Harfler = ["a","f","ü","y","w"]

değer = min(Numaralar)
print(değer)
değer1 = max(Numaralar)
print(değer1)
değer2= max(Harfler)
print(değer2)
değer3=min(Harfler)
print(değer3) #sayılarda küçüktne büyüye, harflerde alfabetik max min alma

say= Numaralar[0:5] #belirtilen indeks arasını al
print(say)


Numaralar[4] = 40
print(Numaralar) #listeler güncellenebilir

Numaralar.append(59) #listeye numara ekleme () içerisine yazılır
Numaralar.insert(3,78) #istenilen konuma istenlilen sayıyı ekler
print(Numaralar)
 
Numaralar.pop(2) #() içerisine yazılan sıradakini siler
print(Numaralar)

Numaralar.remove(123) #verilen değeri siler
print(Numaralar)

Numaralar.sort() #sıralar
print(Numaralar)
Harfler.sort()
print(Harfler)

Numaralar.reverse() #sıraladığımızı ters çevirir büyükten küçüğe yani
print(Numaralar)

print(len(Numaralar)) #kaç tane numara olduğunu soruyoruz

print(Numaralar.count(59)) #() içerisine yazılan ifade o sayıdan kaç tane olduğuna bakar

Numaralar.clear() #listeyi tamamen siler
print(Numaralar) 

 #https://www.w3schools.com/python/python_ref_list.asp
