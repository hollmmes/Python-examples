# sorunla karşılaşıldı ama kodsal bir hata değil expection kullanılabilir try except 
# istisna hatalarda kullanılabilir
try:
    num=int(input("bölünecek sayıyı gir: "))
    num2=int(input("bölecek sayıyı gir: "))
    result= num / num2
    print (result)
except ZeroDivisionError as e: # as e ile hatanın kaynanığı gösteririz
    print(e)
    print ("0a bölemezsin aptl") # hiç hata vermemiş ama kod çalışmamışsa zero div kullanılır

except ValueError as e:
    print(e)
    print("Sayı girsene evladım")
    
except Exception as e:
    print(e)
    print ("Bir hatayla karşılaşıldı :(")
    
else:                   #hata istisnası yoksa yazdır işte
    print (result)
    
finally:
    print("this will always execute") #kodu kapatırkenki yazıyı verir #dosya kontrolünde önemli oalcak
