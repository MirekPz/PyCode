"""
Zadanie wstępne:
- wygenerowanie listy słów do odgadywania w grze

words - baza słów (w formie listy), z której jest losowane słowo do odgadnięcia
źródło danych (plik HTML do przetworzenia):  http://kurs-angielskiego.net/owoce-po-angielsku.php
(uwaga: można wymieniać bazy słów na inne tematy, np.: http://kurs-angielskiego.net/warzywa-po-angielsku.php)

1. zamiana pliku tekstowego na listę, każdy wiersz to jeden element listy
2. usunięcie angielskich określeń, wszytko co jest przed znacznikiem </td><td> łącznie z nim,
  a potem końcowego znacznika </td></tr> ze znakiem nowej linii \n,
  czyli ostatnich 12 znaków z każdego elementu listy, tak by zostały tylko angielskie nazwy owoców

Teraz zadanie właściwe, czyli losowanie wybranego owocu i próba odgadnięcia jego nazwy.

Wykorzystamy konstrukcję random.choice(), czyli losowanie stringów.
"""

import random

fruit = []
with open("fruit_from_website.txt", "r") as fruit_file:
    for line in fruit_file.readlines():
        start_tag = "</td><td>"
        final_tag = "</td></tr>\n"
        position = line.index(start_tag) + len(start_tag)
        line = line[position:]
        line = line[: -len(final_tag)]
        fruit.append(line)

drawn_word = random.choice(fruit).upper()
sign_numbers = len(drawn_word)

print()
print('\t'*3 + '*' * (12 + len("THE HANGMAN GAME")))
print("\t"*3 + "*     THE HANGMAN GAME     *")
print('\t'*3 + '*' * (12 + len("THE HANGMAN GAME")))
print()
print("You can guess only one letter or whole word from the following list: ")

print()
for element in fruit:
    print(element, end='   ')

print("\n\n")
print("START")
print()
print(f"The name of fruit consists of {sign_numbers} letters (can be space or dash inside too).")
print("_ " * sign_numbers)
print()
print("Guess it!")
print()

is_not_guessed_word = True
letter = ""
guessed_word = ""
i = 0

while is_not_guessed_word:

    print()
    letter = input(' ===> ').upper()

    if not letter.isalpha() and not letter == "-" and not letter == " ":
        print("Incorrect sign in word! Try again.")
        print(guessed_word + " _" * (sign_numbers - len(guessed_word)))
        continue

    print(letter)
    print("\t\t\t" + drawn_word)
    if letter == drawn_word.upper():   # odgadnięte całe słowo
        print(letter)
        guessed_word = letter
        print("\nBingo!")
        break

    if letter in drawn_word.upper():
        liczba_wystapien_wpisanej_litery_w_wylosowanym_slowie = drawn_word.count(letter)
        print("Liczba wystąpień wpisanej litery: ", drawn_word.count(letter))  # ile razy wpisana litera występuje w wylosowanym ciągu
        # tyle razy zastosować index(), jaką wartość ma funkcja count()
        print('@@@@@@@@@@')
        pozycja = 0 # zainicjowanie zmiennej
        for n in range(liczba_wystapien_wpisanej_litery_w_wylosowanym_slowie):
            pozycja = drawn_word[pozycja:].index(letter)   ## --------------------------%%%%%%%%%
            print(pozycja)
        # na jakiej pozycji są znalezione litery i podmienić je zamiast kresek !!!!!!!!!!!!!!!!!!!!!*********
        guessed_word = guessed_word + letter
        print(guessed_word + " _" * (sign_numbers - len(guessed_word)))
        i = i + 1
        if i == sign_numbers:
            print("\nBingo!")
            break
    else:
        print("Wrong letter!")
        print(guessed_word + " _" * (sign_numbers - len(guessed_word)))

input("\nPress any key when ready...")
