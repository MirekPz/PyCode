"""
Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
"""

wyraz = input("Wpisz dowolny ciąg znakowy: ")

if len(wyraz) <= 5:
    print("Podany ciąg jest za krótki!")

if 'a' in wyraz:
    print("Ciąg zawiera literę 'a'")
    nowy_ciag = wyraz.replace("a", "z")
    print(nowy_ciag)
