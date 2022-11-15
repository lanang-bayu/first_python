'''
COntoh program perulangan dengan while dengan undefined count
'''

books = 10
books_count = 0
print('Ibu berkata, "Baca bukumu Ranting!')

understood_count = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami = {understood_count} buku")

while books_count < books * 2:
    books_count = books_count + 1
    if understood_count == books - 1:
        print(f"Buku {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == books:
    print('"Bu, semua buku sudah dipahami"')
else:
    print(f'Bu, tidak semua buku bisa dipahami. Ranting hanya bisa memahami {books} buku')
