#import mod_mesaj as ms # her şeyi çağırıyor büyük programda yavaşlığa sebep olabilir
#ms.hello()
#ms.bye()

from mod_mesaj import hello,bye # büyük programlarda kullanıalbilir
hello()
bye()

help("mod_mesaj") #o modülde neler yapabildiğimize bakabiliriz
