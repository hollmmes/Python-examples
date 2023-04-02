import random

print(random.randint(3, 9)) #başlangıç ve son değerleri

mylist=["rock","paper","scissors"] # listeden rastgele seçme
x= random.choice(mylist)
print(x)

cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"] #rastgele karıştırma
random.shuffle(cards)
print(cards)
