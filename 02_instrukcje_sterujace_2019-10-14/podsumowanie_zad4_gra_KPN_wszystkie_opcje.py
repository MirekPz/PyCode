"""
4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
        Użytkownik podaje jedną z 3 figur.
        Komputer losuje jedną z 3 figur.
        Sprawdź kto wygrał tę rundę.
        Zmień kod tak, by użytkownik mógł podać liczbę rund.
        Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
*****   Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’    ******
"""

import random

game_round = int(input("Ile rund chcesz rozegrać: "))

counter = 0
number_of_rounds_won_by_computer = 0
number_of_rounds_won_by_the_user = 0
end_of_game = False

while counter < game_round and not end_of_game:
    counter += 1

    print("\nRunda nr: {}".format(counter))

    # 1. Użytkownik podaje jedną z 3 figur do gry: [K]amień, [P]apier, [N]ożyce
    user_figure = " "
    while True:
        user_figure = input("Wybierz figurę do gry [K, P, N] lub wpisz 'koniec', by zakończyć grę: ").upper()
        if user_figure == "KONIEC":
            print("\nPrzerwanie gry przez użytkownika!")
            end_of_game = True
            break
        elif user_figure == "K":
            print("Użytkownik wybrał KAMIEŃ.")
            break
        elif user_figure == "P":
            print("Użytkownik wybrał PAPIER.")
            break
        elif user_figure == "N":
            print("Użytkownik wybrał NOŻYCE.")
            break
        else:
            print("Niepoprawny wybór figury!")

    if not end_of_game:

        # 2. Komputer losuje jedną z 3 figur
        drawn_figure = random.choice("KPN")
        if drawn_figure == "K":
            print("Komputer wylosował: KAMIEŃ")
        elif drawn_figure == "P":
            print("Komputer wylosował: PAPIER")
        else:
            print("Komputer wylosował: NOŻYCE.")

        # 3. Sprawdzamy kto wygrał tę rundę
        if user_figure == drawn_figure:
            print("*** Remis ***")
        else:
            if user_figure == "P" and drawn_figure == "K":   # papier owija kamień, wygrywa P
                winner = "Użytkownik"
                number_of_rounds_won_by_the_user += 1
            elif user_figure == "P" and drawn_figure == "N":   # nożyce tną papier, wygrywają N
                winner = "Komputer"
                number_of_rounds_won_by_computer += 1
            elif user_figure == "K" and drawn_figure == "N":   # kamień tępi nożyce, wygrywa K
                winner = "Użytkownik"
                number_of_rounds_won_by_the_user += 1
            elif user_figure == "K" and drawn_figure == "P":
                winner = "Komputer"
                number_of_rounds_won_by_computer += 1
            elif user_figure == "N" and drawn_figure == "K":
                winner = "Komputer"
                number_of_rounds_won_by_computer += 1
            elif user_figure == "N" and drawn_figure == "P":
                winner = "Użytkownik"
                number_of_rounds_won_by_the_user += 1
            print("Rundę {} wygrał:".format(counter), winner)

if not end_of_game:
    print("\nŁączna liczba wygranych rund:")
    print("- użytkownik: {}".format(number_of_rounds_won_by_the_user))
    print("- komputer: {}".format(number_of_rounds_won_by_computer))

    if number_of_rounds_won_by_computer > number_of_rounds_won_by_the_user:
        print("\nPojedynek wielorundowy wygrywa KOMPUTER.")
    elif number_of_rounds_won_by_computer < number_of_rounds_won_by_the_user:
        print("\nPojedynek wielorundowy wygrywa UŻYTKOWNIK.")
    else:
        print("\n*** REMIS ***")
