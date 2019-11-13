"""
Znajdź największy wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.
"""

is_number = False

while not is_number:
    print("\nPodaj dwie liczby naturalne:")
    try:
        a = int(input("- pierwsza: "))
        b = int(input("- druga:    "))
        is_number = True
    except ValueError:
        print("\nObie liczby muszą być naturalne! Popraw wpisywane dane.")
    except KeyboardInterrupt:
        print("\n\nWciśnięto niewłaściwą kombinację klawiszy! Wpisz raz jeszcze poprawne liczby.")

number_1 = a
number_2 = b

while a != b:
    if a > b:
        difference = a - b
        a = b
        b = difference
    else:
        difference = b - a
        b = a
        a = difference

if a == b:
    print(f"\nNWD liczb {number_1} i {number_2} to: {a}")
