# set ile benzer key value metodu kullanarak bilgi çağırabiliriz

capitals = {"USA":"Washington DC",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}
print(capitals["Russia"]) # key kullanark çağırdık
print(capitals.get("Germany")) # get ile varsa çağırır yoksa bişi yapmaz daha güvenli
print(capitals.get("USA"))

print(capitals.keys()) #keyleri gösterir
print(capitals.values()) #değerleri gösterir
print(capitals.items()) #her şeyi gösterir

print("-"*50)

for key,value in capitals.items(): #her şeyi gösterir
    print(key,value)
    
capitals.update({"Germany":"Berlin", #update ile yeni şeyler ekleriz, aynı zamanda olanı güncelleyebiliriz
                 "Turkey":"Ankara"})

print(" ")

print(capitals.get("Germany"))
print(capitals.get("Turkey"))

print(" ")

capitals.pop("China") #silme işlemi

for key,value in capitals.items(): 
    print(key,value)
