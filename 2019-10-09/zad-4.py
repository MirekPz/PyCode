"""
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
- Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
- Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
- Połącz dane w jeden ciąg book za pomocą spacji
- Policz liczbę wszystkich znaków w napisie book
"""

title = input("Podaj tytuł książki: ")
author = input("Nazwisko autora: ")
pages = input("Liczba stron: ")
print("_" * 40)

title_without_spaces = title.replace(' ', '')   # title without spaces
print("Czy tylko litery w tytule:", title_without_spaces.isalpha())

author_without_spaces = author.replace(" ", "")  # name of author without spaces
print("Czy tylko litery w nazwisku:", author_without_spaces.isalpha())

print("Czy liczba stron jest liczbą naturalną:", pages.isdigit())

print("Tytuł:", title.capitalize())
print("Autor:", author.title())

book = title + " " + author + " " + str(pages)
print("book = ", book)

print("Liczba znaków w napisie book:", len(book))
