"""
Stwórz grę ciepło zimno.
- Komputer losuje liczbę z zakresu od 1 do 100.
- Użytkownik podaje swój traf.
- Komputer odpowiada ciepło zimno, ale nie więcej niż 6 razy.
- Jeśli użytkownik zgadnie wygrywa gracz.
- Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
"""

import random

number_drawn = random.randrange(1, 101)
print(number_drawn)

counter = 0
while counter < 6:
    number_provided = int(input("Zgadnij wylosowaną liczbę z zakresu od 1 do 100: "))
    counter += 1
    if number_provided == number_drawn:
        print("\nGratulacje! Liczba odgadnięta poprawnie")
        break
    elif number_provided > number_drawn:
        print("\nLiczba za duża.")
        if counter == 6:
            print("\nLiczba prób została wyczerpana!")
    else:
        print("\nLiczba za mała.")
        if counter == 6:
            print("\nLiczba prób została wyczerpana!")

print("\nUWAGA: wylosowano liczbę: ", number_drawn)
