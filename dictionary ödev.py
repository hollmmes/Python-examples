#sözlük ödevi
#database
kelimeler={"kalem": "pen","defter": "notebook", "bilgisayar": "computer", "hesap makinesi": "calculator", "kod": "code", "fare": "mouse", "klavye":"keyboard",
           "pen": "kalem", "notebook": "defter", "computer": "bilgisayar", "calculator": "hesap makinesi", "code": "kod", "mouse": "fare", }


def ceviri(*args, **kwargs):
    for sözcük in args:
        print("{:<10}-> {}".format(sözcük,kwargs[sözcük])) 
        

while True:
    words=input("TR->EN, EN->TR çevirisini istediğiniz kelimeyi giriniz: " )
    if(words=="exit"):
        break
    ceviri(words, **kelimeler)