"""
Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.
"""

filename = "cytaty.txt"

with open(filename, encoding="UTF-8") as file:
    content = file.read()

print(content)

words = content.split()  # jako lista
print(words)
max_length = 0
max_word = ""
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print(max_length)
print(f"Najdłuższe słowo w podanym fragmencie to: {max_word}, zawiera {max_length} znaków")

