sayı=int(input("bir sayı giriniz"))
basamak=int(input("basamak sayısını giriniz"))
toplam=0
i=sayı
for x in range (0,basamak+1):
     rakam=i%10
     toplam+=rakam**basamak
     i//=10
if (sayı==toplam):
     print("bu bir Armstrong sayısıdır")
else:
     print("bu bir Armstrong sayısı değildir")
