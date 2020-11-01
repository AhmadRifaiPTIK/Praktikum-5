import math

#Masukan Nilai

NilaiMatematika = int(input ("Masukan Nilai Matematika :"))

NilaiIpa = int(input ("Masukan Nilai Ipa:"))

NilaiBahasaIndonesia = int(input("Masukan Nilai Bahasa Indonesia:"))

if NilaiMatematika > 0 and NilaiMatematika <101:
     if   NilaiMatematika > 0  and NilaiMatematika < 69:
          StatusKelulusan = 'TIDAK LULUS'
     elif NilaiMatematika > 70 and NilaiMatematika <= 100:
          StatusKelulusan = 'LULUS'
          if NilaiIpa > 0 and NilaiIpa < 101:
                    if NilaiIpa > 0 and NilaiIpa < 59:
                      StatusKelulusan = 'TIDAK LULUS'
                    elif NilaiIpa > 60 and NilaiIpa <= 100:
                         StatusKelulusan = 'LULUS'
                    if NilaiBahasaIndonesia >0 and NilaiBahasaIndonesia <101:
                              if NilaiBahasaIndonesia > 0 and NilaiBahasaIndonesia < 59:
                                   StatusKelulusan = 'TIDAK LULUS'
                              elif (NilaiBahasaIndonesia > 60) and (NilaiBahasaIndonesia <= 100):
                                   StatusKelulusan = 'LULUS'

     print('STATUS KELULUSAN:',StatusKelulusan)
else :
     print("Angka yang anda masukan tidak valid")


