"""
Stwórz grę ciepło zimno.
- Komputer losuje liczbę z zakresu od 1 do 100.
- Użytkownik podaje swój traf.
- Komputer odpowiada ciepło zimno, ale nie więcej niż 6 razy.
- Jeśli użytkownik zgadnie wygrywa gracz.
- Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

Uwaga: wariant z podpowiadaniem zakresu liczb do odgadnięcia, tzn. po podaniu każdej kolejnej liczby zakres zostaje
       zawężony stosownie do uzyskanej odpowiedzi na poprzedni "strzał", np. jeżeli podaliśmy liczbę 50 i komputer mówi,
       że liczba jest za duża, to następne odgadywanie będzie już w zakresie od 1 do 49 zamiast od 1 do 100, itd.
"""

import random

number_drawn = random.randrange(1, 101)
#print(number_drawn)

counter = 0
upper_range = 100
lower_range = 1

while counter < 6:
    number_provided = int(input("Zgadnij wylosowaną liczbę z zakresu od {} do {}: ".format(lower_range, upper_range)))
    counter += 1
    if number_provided == number_drawn:
        print("\nGratulacje! Liczba odgadnięta poprawnie za {} razem.".format(counter))
        break
    elif number_provided > number_drawn:
        print("\nLiczba za duża.")
        upper_range = number_provided - 1
        if counter == 6:
            print("\nLiczba prób została wyczerpana!")
            print("\nUWAGA: wylosowano liczbę: ", number_drawn)
    else:
        print("\nLiczba za mała.")
        lower_range = number_provided + 1
        if counter == 6:
            print("\nLiczba prób została wyczerpana!")
            print("\nUWAGA: wylosowano liczbę: ", number_drawn)
