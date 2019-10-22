"""
Utwórz 2 krotki.
Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki
oraz nieparzystych elementów z drugiej.
"""

list1 = []
for i in range(26):
    list1.append(i)
tuple1 = tuple(list1)

list2 = []
for i in range(26):
    list2.append(chr(97 + i))
tuple2 = tuple(list2)

print('\nPierwsza krotka:')
print(tuple1)
print('\nDruga krotka:')
print(tuple2)

# list3 - parzyste indeksy z tuple1 oraz nieparzyste z tuple2

list3 = []
for i in range(26):
    if i % 2 == 0:
        # parzyste z tupli pierwszej
        list3.append(tuple1[i])
    else:
        # nieparzyste z tupli drugiej
        list3.append(tuple2[i])

print("\nLista po połączeniu elementów o parzystym indeksie z pierwszej krotki oraz elementów o nieparzystym z drugiej:")
print(list3)
