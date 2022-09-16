



#kullanıcı1 ve kullanıcı2 , 1 ve 6 arasından rastgele bir rakam tutar ve tutuğu rakam büyük olan kazanır,skoru ilk önce 3 olan oyunun kazananı olur.
import random
import time

kullanici1Skor = 0
kullanici2Skor = 0


while True:
    kullanici1= random.randint(1,6)
    print("kullanıcı 1 : ",kullanici1 )
    time.sleep(1.8)
    kullanici2 = random.randint(1,6)
    print("Kullanıcı 2: ", kullanici2)
    time.sleep(1.8)
    if kullanici1> kullanici2:
        print("Kullanıcı 1 kazandı.")
        kullanici1Skor += 1
    elif kullanici2 > kullanici1:
        print("Kullanıcı 2 kazandı.")
        kullanici2Skor += 1
    else:
        print("Berabere bitti.")

   
    if kullanici1Skor == 3 or kullanici2Skor == 3:
        print("Kullanıcı 1 :",kullanici1Skor, " - ", kullanici2Skor, ": Kullanıcı 2")

        input()
