print("MERHABA")
print("Dikkat:Şifreniz büyük harf,küçük harf,rakam ve özel karakterlerin her birinden en az bir tane içermelidir!")

buyukharf="ABCDEFGHIJKLMNOPRSTUVYZWXYZ"
kucukharf="acbdefghijklmnoprstuvyzwxyz"
rakam="1234567890"
karakter="*?-+."

bhs=0
khs=0
rs=0
ks=0

sifre=input("Şifre giriniz:")

for b in sifre:
    if b in buyukharf:
        bhs+=1
print("Büyük harf sayısı=",bhs)
        
for k in sifre:
    if k in kucukharf:
        khs+=1
print("Küçük harf sayısı=",khs)

for r in sifre:
    if r in rakam:
        rs+=1
print("Rakam sayısı=",rs)

for ok in sifre:
    if ok in karakter:
        ks+=1
print("Karakter sayısı=",ks)

  
for i in sifre:
    if i in buyukharf:
        bhs+=1
    if i in kucukharf:
        khs+=1
    if i in rakam:
        rs+=1
    if i in karakter:
        ks+=1
if(khs==0 or bhs==0 or rs==0 or ks==0):
    print("ŞİFRENİZ GÜVENLİ DEĞİL")
else:
    print("ŞİFRENİZ GÜVENLİ")
while True:
        pass
    
