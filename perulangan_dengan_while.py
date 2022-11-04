'''
COntoh program perulangan dengan while
'''

jumlah_buku = 10
print('Ibu berkata, "Baca bukumu Ranting!')

jumlah_buku_terbaca = 0
print(f'Jumlah buku terbaca = {jumlah_buku_terbaca} buku')

while jumlah_buku_terbaca < jumlah_buku:
    jumlah_buku_terbaca = jumlah_buku_terbaca + 1
    print(f'Buku ke {jumlah_buku_terbaca} sudah terbaca')

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_terbaca}')
