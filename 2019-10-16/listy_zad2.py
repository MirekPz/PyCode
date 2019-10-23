"""
Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""

lista = []
for number in range(10):
    element = int(input("Podaj " + str(number + 1)+" liczbę: "))
    if element % 2 == 1:
        lista.append(element)

print(lista)
