import math

#Masukan Nilai

NilaiMatematika = int(input ("Masukan Nilai Matematika :"))

NilaiIpa = int(input ("Masukan Nilai Ipa:"))

NilaiBahasaIndonesia = int(input("Masukan Nilai Bahasa Indonesia:"))

TotalNilai = NilaiMatematika + NilaiBahasaIndonesia + NilaiIpa

if (NilaiMatematika < 70):
     print("STATUS KELULUSAN :TIDAK LULUS")
elif (NilaiIpa < 60):
     print("STATUS KELULUSAN :TIDAK LULUS")
elif (NilaiBahasaIndonesia < 60):
     print("STATUS KELULUSAN :TIDAK LULUS")
else:
    print("STATUS KELULUSAN :LULUS")

