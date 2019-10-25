"""
Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej
75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność
w kategorii tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
            dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
            ponownie wyświetl zmieniony słownik
    Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu
    również od jego oryginalności. Dopisz odpowiednie komunikaty.
"""

import datetime

cars = {
        'marka': 'Fiat',
        'model': 'Seicento',
        'rocznik': 1999
        }

print()
print("Stan początkowy słownika:")
print(cars)

cars['czy_oryginalny'] = True

print(cars)
print()

print("Sprawdzenie samochodu klienta")
car_brand = input("Marka samochodu: ")
cars['marka'] = car_brand
car_model = input("Model: ")
cars['model'] = car_model
year = int(input("Rocznik: "))
cars['rocznik'] = year
current_year = datetime.date.today().year
car_age = current_year - cars['rocznik']

if car_age >= 25:
    print("Samochód spełnia kryterium wieku.")
    original_parts = int(input("Podaj procent oryginalnych części: "))
    if original_parts >= 75:
        cars['czy_oryginalny'] = True
        print()
        print(f"Gratulacje! Twój samochód {cars['marka'] + ' ' + cars['model']} może być zarejestrowany jako zabytek.")
    else:
        cars['czy_oryginalny'] = False
        print()
        print(f"Niestety Twój samochód {cars['marka'] + ' ' + cars['model']} nie może być zarejestrowany jako samochód zabytkowy.")
        print("Posiada zbyt mało oryginalnych części.")
else:
    print()
    print(f"Twój samochód {cars['marka'] + ' ' + cars['model']} jest jeszcze zbyt młody.")
