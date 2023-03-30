# liste gibilerdir ama çağrılırlar ve değiştirilemezler.

student = ("Tufancan",20,"Errrkek")

print(student.count("Tufancan")) # kaç tane var
print(student.index("Errrkek")) #	kaçıncı sıra

for x in student:
    print(x)
    
if "Errrkek" in student:
    print("oyy bu erkek")
