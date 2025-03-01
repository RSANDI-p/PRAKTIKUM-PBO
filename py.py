file = open("Me.txt", "w")

tulis = input("\nmasukan nama : ")
nim = int(input("masukan NIM : "))
resolusi = input("masukan resolusi tahun ini : ")

file.write(f"\nNama : {tulis}")
file.write(f"\nNIM : {nim}")
file.write(f"\nResosolusi tahun ini : {resolusi}")
print(f"file {file} telah dibuat.")

file.close()

f = open("Me.txt", "r")
print(f. read())


