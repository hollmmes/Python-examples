# liste mantığı ama değerler karışık gelebilir  indexleri yok ve aynı değerleri yok sayar

cars = {"tank","tank","tank","auid","any car name","ummm"}


cars.add("plane")
cars.remove("ummm")
# cars.xxxx 

for x in cars:
    print(x)


print("-"*50)


things = {"bowl","plate","cup","knife"}
cars.update(things)

for x in cars:
    print(x)
    
print("-"*50)

mixed = cars.union(things)
for x in mixed:
    print(x)
    
    # ek not, .difference ile farkılıkları, intersection ile benzerlikleri çekebilrisin
