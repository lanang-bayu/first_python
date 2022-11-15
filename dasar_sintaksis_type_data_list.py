daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
print("Tampilan variable daftar_buku :")
print(daftar_buku)

print("\nProses semua list dengan for in :")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan daftar_buku dengan indeks tertentu :")
print(daftar_buku[0])
print(daftar_buku[3])

print("\nTampilkan dengan for in range :")
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# dynamic type variable untuk daftar_buku
daftar_buku = [1, 'One Piece 352', 354, 3.14]
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda :")
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# kembalikan dynamic type variable untuk daftar_buku di awal
print("\nKembalikan nilai awal daftar_buku")
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nTambahkan 1 buku baru :")
daftar_buku.append('Startup Guidebook')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear List :")
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti elemen pertama :")
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
daftar_buku[0] = 'Kebelet Power'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-1 dengan perintah pop:')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ndata yang diambil pop tadi :')
print(buku)

print('\nPop :')
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -2 :')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
daftar_buku.pop(-2)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

