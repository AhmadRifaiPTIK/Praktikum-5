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

#Gaji Bersih

GajiBersihA = GajiPokokA - PotonganA
GajiBersihB = GajiPokokB - PotonganB
GajiBersihC = GajiPokokC - PotonganC
GajiBersihD = GajiPokokD - PotonganD


# input nama karyawan

kode = input("Masukan Kode Karyawan")
nama = input("Masukan Nama Karyawan")
golongan = input("Masukan Golongan karyawan")

time.sleep(3)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Struktur Rincian Gaji Karyawan")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# tampilan Nama Karyawan
print("Nama Karyawan    :", nama, "(Kode:",kode,")")
print("Golongan         :",golongan)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)


if (golongan=='A') :
    print("Gaji Pokok           : Rp",GajiPokokA)
    print("Potongan(",PotGolA,") : Rp",PotonganA)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    print("Gaji Bersih          : Rp",GajiBersihA)
if (golongan=='B'):
        print("Gaji Pokok           : Rp",GajiPokokB)
        print("Potongan(",PotGolB,") : Rp",PotonganB)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3)
        print("Gaji Bersih          : Rp",GajiBersihB)
if (golongan=='C'):
        print("Gaji Pokok           : Rp",GajiPokokC)
        print("Potongan(",PotGolC,") : Rp",PotonganC)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3)
        print("Gaji Bersih          : Rp",GajiBersihC)
if (golongan=='D'):
        print("Gaji Pokok           : Rp",GajiPokokD)
        print("Potongan(",PotGolD,") : Rp",PotonganD)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3)
        print("Gaji Bersih          : Rp",GajiBersihD)