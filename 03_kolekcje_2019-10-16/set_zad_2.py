"""
Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
"""

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

print("Lista:", L_test)
print("Tupla:", T_test)
print("Set:  ", S_test)
print(20 * '-')

# append()
L_test.append('append')
print(L_test)
# tuple, set - nie działa

# extend()
L_test.extend(['extend', 'extend', 'extend', 2, 2, 2, 2, 2, 2])
print(L_test)
# tuple, set - nie działa

# insert()
L_test.insert(2, 'insert')
print(L_test)
# tuple, set - nie działa

# remove()
L_test.remove(1)
L_test.remove('extend')
print(L_test)
# tuple, set - nie działa

# index()
print('Lista: ', L_test.index(3))
print('Tupla: ', T_test.index(3))
# nie działa tylko dla 'set' (bo elementy kolekcji 'set' są nieuporządkowane)

# count()
print('Lista: ', L_test.count(2))
print('Tupla: ', T_test.count(2))
# nie działa tylko dla 'set' (bo 'set' operuje na elementach unikalnych i dochodziłoby do sprzeczności w liczeniu
# elementów, np. {1, 1, 1, 1, 2} oraz {1, 2, 2, 2} sprowadzone by zostało do {1, 2}

# pop()
print(L_test.pop(4))
print(L_test)

# dla tupli pop() nie działa

print(S_test)
print(S_test.pop())   # pop() jest bezargumentowe dla 'setu', można usunąć tylko pierwszy element 'setu'
print(S_test)

# reverse()
L_test.reverse()
print(L_test)
# tuple, set - nie działa ("tuple' jest niemodyfikowalna, 'set' jest nieuporządkowany)

# len
print(len(L_test))
print(len(T_test))
print(len(S_test))
