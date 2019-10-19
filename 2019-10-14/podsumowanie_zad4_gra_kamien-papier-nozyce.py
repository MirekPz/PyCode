"""
4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
        Użytkownik podaje jedną z 3 figur.
        Komputer losuje jedną z 3 figur.
        Sprawdź kto wygrał tę rundę.
        Zmień kod tak, by użytkownik mógł podać liczbę rund.
        Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
"""

import random

# 1. Użytkownik podaje jedną z 3 figur do gry: [K]amień, [P]apier, [N]ożyce
user_figure = " "
while True:
    user_figure = input("Wybierz figurę do gry [K, P, N]: ").upper()
    if user_figure == "K":
        print("Wybrano KAMIEŃ.")
        break
    elif user_figure == "P":
        print("Wybrano PAPIER.")
        break
    elif user_figure == "N":
        print("Wybrano NOŻYCE.")
        break
    else:
        print("Niepoprawny wybór figury!")

# 2. Komputer losuje jedną z 3 figur
drawn_figure = random.choice("KPN")
if drawn_figure == "K":
    print("Komputer wylosował: KAMIEŃ")
elif drawn_figure == "P":
    print("Komputer wylosował: PAPIER")
else:
    print("Komputer wylosował: NOŻYCE.")

# 3. Sprawdzamy kto wygrał tę rundę


