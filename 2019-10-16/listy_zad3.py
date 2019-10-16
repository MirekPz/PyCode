"""
Dla podanej przez użytkownika listy liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
"""

lista = []
while True:
    element = input("Podaj liczbę całkowitą [samo Enter - koniec]: ")
    if element == "":
        break
    element = int(element)
    lista.append(element)

print(lista)

if lista[0] == lista[-1]:
    print("Pierwszy i ostatni element są takie same")
else:
    print("Skrajne elementy są różne")
