# eğer yazdığın program kısaysa aynı dosyada uzunsa ayırarak yaz
class Car:
    def __init__(self,model,yıl,color):
        self.model= model
        self.yıl=yıl
        self.color=color 
        
    def drive(self):
        print(self.model+" sürülüyor")
    def stop(self):
        print(self.model+" durduruluyor")

car_1=Car("Corvette",1990,"Kırmızı")
car_2=Car("Mustang",2010,"Mavi")

print(car_1.model, end=" ")
print(car_1.yıl, end=" ")
print(car_1.color)
print(car_2.model, end=" ")
print(car_2.yıl, end=" ")
print(car_2.color)

print("-"*50)

car_1.drive()
car_2.drive()
car_1.stop()
car_2.stop()
