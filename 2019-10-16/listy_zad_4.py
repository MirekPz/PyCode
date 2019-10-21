"""
Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
"""

while True:
    number_of_elements = input("\nPodaj planowaną liczbę elementów do wpisania (musi być parzysta): ")
    if not number_of_elements.isdigit():
        print("Błąd! \nTo nie jest liczba!")
        continue
    number_of_elements = int(number_of_elements)
    if number_of_elements % 2 == 1:
        print("Błąd! \nTo jest liczba nieparzysta.")
        continue
    print()
    break

elements = []
print("Pobieranie elementów listy:")
for element in range(number_of_elements):
    element = input("- wpisz kolejną wartość: ")
    elements.append(element)

print("\nUtworzono następującą listę elementów:")
print(elements)

print("\nElementy środkowe to:")
middle1 = elements[int(len(elements)/2 - 1)]
middle2 = elements[int(len(elements)/2)]
print(middle1)
print(middle2)

if middle1 == middle2:
    print("Elemety środkowe są takie same.")
else:
    print("Elementy środkowe są różne.")
