"""
Napisz funkcję, która zapyta o ocenę książki i wyświetli książkę wraz z oceną,
"""

def add_book():
    dict_books = {}
    counter = int(input("Ile książek chcesz dodać: "))
    for _ in range(counter):
        title = input("Podaj tytuł książki: ")
        grade = int(input("Jak oceniasz książkę [1..10]: "))
        dict_books[title] = grade
    return dict_books

def read_book_by_grade(libr):
    g = int(input("Podaj ocenę książki, jaką chcesz przeczytać: "))
    if g in libr.values():
        for title, grade in libr.items():
            if grade == g:
                print(title, "- ocena: ", grade)
    else:
        print("Nie ma książki o takiej ocenie")

books = add_book()
print(books)

read_book_by_grade(books)
