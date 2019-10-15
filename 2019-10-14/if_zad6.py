"""
Zapytaj użytkownika o numer od 1 do 100,
jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
w przeciwnym razie wyświetl “pudło!”
"""

hidden_number = 50

user_number = input("\nPodaj liczbę z przedziału <1...100>: ")

if not user_number.isdigit():
    print("To nie jest liczba!")
elif int(user_number) == hidden_number:
    print("Gratulacje!")
else:
    print("Pudło!")
