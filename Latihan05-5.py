import time

#Gaji Pokok

GajiPokokA = 10000000
GajiPokokB = 8500000
GajiPokokC = 7000000
GajiPokokD = 5500000

#Potongan Golongan

PotGolA    = 25/1000
PotGolB    = 20/1000
PotGolC    = 15/1000
PotGolD    = 10/1000

#hitungan potongan

PotonganA = GajiPokokA * PotGolA
PotonganB = GajiPokokB * PotGolB
PotonganC = GajiPokokC * PotGolC
PotonganD = GajiPokokD * PotGolD



# input nama karyawan

kode = input("Masukan Kode Karyawan :")

nama = input("Masukan Nama Karyawan :")

golongan = input("Masukan Golongan karyawan :")

print("Status Menikah : 1:Sudah \n 2:Belum")

StatusMenikah = input("Masukan Status Menikah :")

if StatusMenikah=='1':
      Jumlah_Anak = int(input("Masukan Jumlah Anak :"))

time.sleep(4)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Struktur Rincian Gaji Karyawan")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# tampilan Nama Karyawan
print("Nama Karyawan    :", nama, "(Kode:",kode,")")
print("Golongan         :",golongan)
if StatusMenikah=='1':
    print("Status Menikah   : Menikah")
if StatusMenikah=='2':
    print("Status Menikah   : Belum  ")
if StatusMenikah=='1':
    print("Jumlah Anak  :",Jumlah_Anak)
if StatusMenikah=='2':
    print("Jumlah Anak  : 0")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)



#Tunjangan Istri
TunjanganIstriA = 1/10 * GajiPokokA
TunjanganIstriB = 1/10 * GajiPokokB
TunjanganIstriC = 1/10 * GajiPokokC
TunjanganIstriD = 1/10 * GajiPokokD


if StatusMenikah=='1':
    TunjanganIstriA = 1/10 * GajiPokokA
    TunjanganIstriB = 1/10 * GajiPokokB
    TunjanganIstriC = 1/10 * GajiPokokC
    TunjanganIstriD = 1/10 * GajiPokokD

if StatusMenikah=='2':
    TunjanganIstriA = 1 / 10 * GajiPokokA *0
    TunjanganIstriB = 1 / 10 * GajiPokokB *0
    TunjanganIstriC = 1 / 10 * GajiPokokC *0
    TunjanganIstriD = 1 / 10 * GajiPokokD *0

#Tunjangan Anak
TunjanganAnakA = 1/20 * GajiPokokA
TunjanganAnakB = 1/20 * GajiPokokB
TunjanganAnakC = 1/20 * GajiPokokC
TunjanganAnakD = 1/20 * GajiPokokD

if StatusMenikah=='1':
    if Jumlah_Anak=='1':
        TunjanganAnakA = 1/20 * GajiPokokA *1
        TunjanganAnakB = 1/20 * GajiPokokB *1
        TunjanganAnakC = 1/20 * GajiPokokC *1
        TunjanganAnakD = 1/20 * GajiPokokD *1
    elif Jumlah_Anak=='2':
        TunjanganAnakA = 1/20 * GajiPokokA *2
        TunjanganAnakB = 1/20 * GajiPokokB *2
        TunjanganAnakC = 1/20 * GajiPokokC *2
        TunjanganAnakD = 1/20 * GajiPokokD *2
    elif Jumlah_Anak=='3':
        TunjanganAnakA = 1/20 * GajiPokokA *3
        TunjanganAnakB = 1/20 * GajiPokokB *3
        TunjanganAnakC = 1/20 * GajiPokokC *3
        TunjanganAnakD = 1/20 * GajiPokokD *3
    elif Jumlah_Anak=='4':
        TunjanganAnakA = 1/20 * GajiPokokA *4
        TunjanganAnakB = 1/20 * GajiPokokB *4
        TunjanganAnakC = 1/20 * GajiPokokC *4
        TunjanganAnakD = 1/20 * GajiPokokD *4

if StatusMenikah=='2':
    TunjanganAnakA = 1/20 * GajiPokokA *0
    TunjanganAnakB = 1/20 * GajiPokokB *0
    TunjanganAnakC = 1/20 * GajiPokokC *0
    TunjanganAnakD = 1/20 * GajiPokokD *0

#Gaji Kotor
GajiKotorA = GajiPokokA + TunjanganIstriA + TunjanganAnakA
GajiKotorB = GajiPokokB + TunjanganIstriB + TunjanganAnakB
GajiKotorC = GajiPokokC + TunjanganIstriC + TunjanganAnakC
GajiKotorD = GajiPokokD + TunjanganIstriD + TunjanganAnakD

#Gaji Bersih

GajiBersihA = GajiKotorA - PotonganA
GajiBersihB = GajiKotorB - PotonganB
GajiBersihC = GajiKotorC - PotonganC
GajiBersihD = GajiKotorD - PotonganD

if (golongan=='A') :
    print("Gaji Pokok           : Rp",GajiPokokA)
    print("Tunjangan Istri/Suami: Rp",TunjanganIstriA)
    print("Tunjangan Anak       : Rp",TunjanganAnakA)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gaji Kotor           : Rp",GajiKotorA)
    print("Potongan(",PotGolA,") : Rp",PotonganA)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print("Gaji Bersih          : Rp",GajiBersihA)
elif (golongan=='B') :
    print("Gaji Pokok           : Rp",GajiPokokB)
    print("Tunjangan Istri/Suami: Rp",TunjanganIstriB)
    print("Tunjangan Anak       : Rp",TunjanganAnakB)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gaji Kotor           : Rp",GajiKotorB)
    print("Potongan(",PotGolB,") : Rp",PotonganB)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print("Gaji Bersih          : Rp",GajiBersihB)
elif (golongan=='C') :
    print("Gaji Pokok           : Rp",GajiPokokC)
    print("Tunjangan Istri/Suami: Rp",TunjanganIstriC)
    print("Tunjangan Anak       : Rp",TunjanganAnakC)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gaji Kotor           : Rp",GajiKotorC)
    print("Potongan(",PotGolC,") : Rp",PotonganC)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print("Gaji Bersih          : Rp",GajiBersihC)
elif (golongan=='D') :
    print("Gaji Pokok           : Rp",GajiPokokD)
    print("Tunjangan Istri/Suami: Rp",TunjanganIstriD)
    print("Tunjangan Anak       : Rp",TunjanganAnakD)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gaji Kotor           : Rp",GajiKotorD)
    print("Potongan(",PotGolD,") : Rp",PotonganD)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print("Gaji Bersih          : Rp",GajiBersihD)