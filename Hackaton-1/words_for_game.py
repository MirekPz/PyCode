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

drawn_word = random.choice(fruit)
sign_numbers = len(drawn_word)

print()
print("THE HANGMAN GAME")
print()
print(f"The name of fruit consists of {sign_numbers} letters (can be space or dash too inside).")
print("Guess it!")
print("_ " * sign_numbers)
print()
print("Your turn now... You can guess only one letter or whole word: ")
letter = input().upper()
print(letter)
if not letter.isalpha() or letter == "-" or letter == " ":
    print("Incorrect sign in word! Try again.")


print("\nMy prompt: ", drawn_word, sign_numbers)

