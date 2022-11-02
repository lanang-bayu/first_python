'''
Contoh program perulangan dengan for
'''

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu Budi!"')
jumlah_buku_dibaca=0
print(f"Jumlah buku yang sudah dibaca Budi = {jumlah_buku_dibaca} buku")

print("Dengan for")
for jumlah_buku_dibaca in range (1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca Budi = {jumlah_buku_dibaca} buku")
print("Selesai")
