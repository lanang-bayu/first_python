# List Comprehension
print('\nperintah Del :')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
del daftar_buku[0]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension :')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
del daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension dengan start :')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
del daftar_buku[0:-1] # START:END
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension dengan start end step :')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
del daftar_buku[0::2] # START:END:STEP
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension : baru ')
daftar_buku = ['The Power of Kepepet', 'Persuasive Copywriting', 'Seni Hidup Minimalis', 'Jurus Sehat Rasulullah']
daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 The Power of Kepepet', '2 Persuasive Copywriting', '3 Seni Hidup Minimalis', '4 Jurus Sehat Rasulullah']
daftar_buku_baru = daftar_buku[0::2] # START:END:STEP
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : genap ')
daftar_buku = ['1 The Power of Kepepet', '2 Persuasive Copywriting', '3 Seni Hidup Minimalis', '4 Jurus Sehat Rasulullah']
daftar_buku_baru = daftar_buku[1::2] # START:END:STEP
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ujung dibuang')
daftar_buku = ['1 The Power of Kepepet', '2 Persuasive Copywriting', '3 Seni Hidup Minimalis', '4 Jurus Sehat Rasulullah']
daftar_buku_baru = daftar_buku[0:-1:2] # START:END:STEP
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ujung dibuang (cara cetak layar lainnya) ')
daftar_buku = ['1 The Power of Kepepet', '2 Persuasive Copywriting', '3 Seni Hidup Minimalis', '4 Jurus Sehat Rasulullah']
print(daftar_buku[0:-1:2]) # START:END:STEP)