import os
# operating system = os , 
# path içerisinde oluşturduğunuz txt dosyasının yerini belirtin ve içine bir şeyler yazın

path ="C:\\Users\\tfnca\\Desktop\\Yazılım\\pyt\\test\\test.txt" #aynı klasörde iseler sadece isim ve format yeterli

if os.path.exists(path):
    print("Böyle bir yer var evet")
    if os.path.isfile(path):
        print("Bu bir dosya evt")
    elif os.path.isdir(path):
        print("bu bir klasör")
else:
    print("Böyle bir yer yok")
    
print("-"*50)

    

text=("Buraya yazdılıracak şeyler\ntxt dosyasının içerisine işlenecektir\ninput ile de çalışabilirz")
try: # try except ile dosya eğer orada yoksa yok diyoz
    with open("C:\\Users\\tfnca\\Desktop\\Yazılım\\pyt\\test\\test.txt","w") as file:
        file.write(text)

    with open("C:\\Users\\tfnca\\Desktop\\Yazılım\\pyt\\test\\test.txt") as file: 
        print(file.read())
except FileNotFoundError:
    print("Dosya bulunamadı :(")
    
