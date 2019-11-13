"""
Znajdź największy wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.
"""

is_number = False

while not is_number:
    print("\nPodaj dwie liczby naturalne:")
    try:
        number_1 = int(input("- pierwsza: "))
        number_2 = int(input("- druga:    "))
        is_number = True
    except ValueError:
        print("\nObie liczby muszą być naturalne! Popraw wpisywane dane.")
    except KeyboardInterrupt:
        print("\n\nWciśnięto niewłaściwą kombinację klawiszy! Wpisz raz jeszcze poprawne liczby.")


def NWD(a, b):
    while a != b:
        if a > b:
            difference = a - b
            a = b
            b = difference
        else:
            difference = b - a
            b = a
            a = difference
    return a


print(f"\nNajwiększy Wspólny Dzielnik liczb {number_1} i {number_2} to: {NWD(number_1, number_2)}")
