import math

#Masukan Nilai

NilaiMatematika = int(input ("Masukan Nilai Matematika :"))

NilaiIpa = int(input ("Masukan Nilai Ipa:"))

NilaiBahasaIndonesia = int(input("Masukan Nilai Bahasa Indonesia:"))

if NilaiMatematika > 0 and NilaiMatematika <101:
     if   NilaiMatematika >= 0  and NilaiMatematika <= 69:
          StatusKelulusan = 'TIDAK LULUS'
     elif NilaiMatematika >= 70 and NilaiMatematika <= 100:
          StatusKelulusan = 'LULUS'
          if NilaiIpa > 0 and NilaiIpa < 101:
                    if NilaiIpa >= 0 and NilaiIpa <= 59:
                      StatusKelulusan = 'TIDAK LULUS'
                    elif NilaiIpa >= 60 and NilaiIpa <= 100:
                         StatusKelulusan = 'LULUS'
                    if NilaiBahasaIndonesia >= 0 and NilaiBahasaIndonesia <=101:
                              if NilaiBahasaIndonesia >= 0 and NilaiBahasaIndonesia <= 59:
                                   StatusKelulusan = 'TIDAK LULUS'
                              elif (NilaiBahasaIndonesia >= 60) and (NilaiBahasaIndonesia <= 100):
                                   StatusKelulusan = 'LULUS'
else :
     print("Angka yang anda masukan tidak valid")
print('STATUS KELULUSAN:',StatusKelulusan)

print("Sebab:")

if NilaiMatematika < 70:
    print("-Nilai Matematika Kurang dari 70")
if NilaiIpa < 60:
    print("-Nilai Ipa Kurang dari 60")
if NilaiBahasaIndonesia < 60:
    print("-Nilai Bahasa Indonesia Kurang dari 60")
else:
    print("Semua Nilai Diatas KKM")
