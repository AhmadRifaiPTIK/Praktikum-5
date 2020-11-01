#Kotak bintang ajaib
kolom = 5
baris = 5
i = 0
while (i < baris):
    j = 0
    while (j < kolom - baris + 1):
        print("*", end=" ")
        j += 1
    print("")
    kolom += 1
    i += 1