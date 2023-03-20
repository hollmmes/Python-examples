
# while döngüsü sınırsızken, for döngüsü sınırlıdır kullanımı buna göre ayır
 
# while döngüsü doğru olduğu sürece devam edecektir

# değer almadığı sürece sormaya devam edecek

name = ""

while len(name) == 0:
    name = input("Enter your name: ")
    
print("Hello " +name)
