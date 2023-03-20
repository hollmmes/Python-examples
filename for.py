import time
# while döngüsü sınırsızken, for döngüsü sınırlıdır kullanımı buna göre ayır
 
 

for i in range(10): #	10a ulaşana kadar yaz dahillik olmaz en son yazılanda!
    print(i)
    
    
    
for i in range(50,100+1,10): #50den 100e kadar sayma 3. virgül ile birlikte kaçar kaçar gideceğine karar veririz
    print(i)
    
    
for i in "Tufancan":
    print(i)


for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("10dan geriye sayma programı xd") # <---- burada da yazdığı gibi
