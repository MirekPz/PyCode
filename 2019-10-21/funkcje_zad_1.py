"""
Napisz funkcję, która pyta użytkownika o pary 'książka + ocena' i zapisuje je w programie.
"""


def add_book(dict_books):
    counter = int(input("Ile książek chcesz dodać: "))
    for _ in range(counter):
        title = input("Podaj tytuł książki: ")
        grade = int(input("Jak oceniasz książkę [1..10]: "))
        dict_books[title] = grade
    return dict_books


books = {}
books = add_book(books)
print(books)
