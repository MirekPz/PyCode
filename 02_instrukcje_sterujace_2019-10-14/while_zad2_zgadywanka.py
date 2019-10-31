"""
Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
(np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
"""

secret_number = 5
user_number = 9999

while user_number != secret_number:
    user_number = input("Podaj liczbę naturalną z zakresu [0...20]: ")
    if not user_number.isdigit():
        print("To nie jest liczba naturalna!")
        continue
    user_number = int(user_number)
    if user_number > 20:
        print("Liczba poza dopuszczalnym zakresem!")

print("Gratuluję odgadnięcia liczby!")
