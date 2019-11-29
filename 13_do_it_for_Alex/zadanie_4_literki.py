"""
Literki 🔠
Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj zadanie na dwa sposoby - za pomocą pętli oraz przez string slicing ( ‘abrakadabra’ -> ‘baaar’).
"""


def even(text):
    print(text[1::2])


text = input("Podaj tekst: ")
even(text)

for i in range(len(text)):
    if (i+1) % 2 == 0:   # indeksujemy od zera, dlatego musi być i+1
        print(text[i], end="")

