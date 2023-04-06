# dec to bin three diff way
# eforsuz yol

number = int(input("Sayi giriniz: "))
print("{}'in binary karşılığı: {:b}".format(number,number)) #bin çevirme

#eforlu yol
print("-"*50)
n = int(input("Sayı giriniz: "))
binary = ""
while n > 0:
    temp = n % 2
    binary=(temp)
    print(binary,end="")
    n = n // 2
        
#fonksiyonlu yol
print("\n","-"*50)
def dectobin(n1):
    binary = ''
    while n1 > 0:
        temp1 = n1 % 2
        binary = str(temp1) + binary
        n1 = n1 // 2
    return binary

decimal = int(input("Sayı giriniz: "))
binary = dectobin(decimal)
print(f"{decimal}'in binary karşılığı: ",binary)
print("\n","-"*50)

