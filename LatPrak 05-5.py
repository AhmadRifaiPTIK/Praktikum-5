
#Pemilihan Bilangan Random
from random import randint
i = 0
while True:
    bil = randint(0, 100)
    i += 1
    if (i > 0):
        break


#Interface

print("Halo Tuan dan Nona , saya telah memilih sebuah angka dari 0 s/d 100 secara acak Silahkan ditebak ya!!")

while True:
    Tebakan = int(input("Tebakan anda       :"))
    if Tebakan < bil:
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
    if Tebakan > bil:
        print("Hehehe… Bilangan tebakan anda terlalu besar")
    if Tebakan == bil :
        print("Yeeee… Bilangan tebakan anda BENAR :-)")
        break