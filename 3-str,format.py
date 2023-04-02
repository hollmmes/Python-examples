name = "Ali Nazik"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:25} nice to mmet you".format(name))
print("Hello, my name is {:<25} nice to mmet you".format(name))
print("Hello, my name is {:>25} nice to mmet you".format(name))
print("Hello, my name is {:^25} nice to mmet you".format(name))

number = 3131
pi = 3.14159265359
print("Number is : {:.2f}".format(pi)) # virgülden sonra kaç şey
print("Number is : {:.4f}".format(pi)) 
print("Number is : {:b}".format(number)) #bin çevirme
print("Number is : {:o}".format(number)) #octa
print("Number is : {:x}".format(number)) #hexa
print("Number is : {:e}".format(number))
