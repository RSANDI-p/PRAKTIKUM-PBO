#RIYAN SANDI PRAYOGA
#123140176
# PBO RD -> RC

data_siswa = {}
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))  
    data_siswa[nama] = nilai 

print("\nDictionary =", data_siswa)
