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
