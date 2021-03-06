"""
 Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
    Program zacznie ze stworzonym słownikiem o trzech kluczach:
            marka (str)
            model (str)
            rocznik (int)
    Wypisze ten słownik na ekran (bez żadnego formatowania)
    Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
        “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
    Jeśli nie spełnia powyższego warunku, wypisze komunikat:
        “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
    Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
    aby zobaczyć, czy program również zmienia swoje zachowanie.
"""

import datetime


def old_cars(brand, model, vintage):
    cars = {
        'marka': brand,
        'model': model,
        'rocznik': vintage
    }
    car_age = datetime.date.today().year - cars['rocznik']
    print()
    if car_age >= 25:
        print(f"Gratulacje! Twój samochód {cars['marka'] + ' ' + cars['model']} może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {cars['marka'] + ' ' + cars['model']} jest jeszcze zbyt młody.")


old_cars('Fiat', 'Seicento', 1999)
old_cars('Porsche', '911 Turbo', 1979)
