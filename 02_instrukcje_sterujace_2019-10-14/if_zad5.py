"""
Stwórz zmienną password.
Hasło powinno składać z liter i cyfr, zwierać co najmniej 1 dużą literę i mieć długość co najmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
Wyświetl różne komunikaty w zależności od rodzaju błędu.
"""

password = input("Nowe hasło: ")

if len(password) < 8:
    print('Hasło za krótkie!')
if not password.isalnum():
    print("Hasło nie może zawierać innych znaków niż litery lub cyfry.")
if password.isalpha():
    print("Hasło nie może mieć samych liter")
if password.isdigit():
    print("Hasło nie może mieć samych cyfr.")
if password.isalnum() and password.islower():
    print("Wszystkie litery nie mogą być małe")
