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


## dokończyć..


if a == b:
    print(f"\nNWD liczb {a} i {b} to: {a}")

