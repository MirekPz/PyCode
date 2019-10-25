"""
Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
- funkcja, wersja 2
"""

import datetime


def old_cars(brand, model, vintage):
    cars = {
        'marka': brand,
        'model': model,
        'rocznik': vintage
    }
    print()
    print(cars)
    car_age = datetime.date.today().year - cars['rocznik']
    if car_age >= 25:
        print(f"Gratulacje! Twój samochód {cars['marka'] + ' ' + cars['model']} może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {cars['marka'] + ' ' + cars['model']} jest jeszcze zbyt młody.")


old_cars('Fiat', 'Seicento', 1999)
old_cars('Porsche', '911 Turbo', 1979)