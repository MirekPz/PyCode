"""
Otwórz dowolny plik np. tekst.txt i wklej do niego fragment inwokacji Pana Tadeusza
"""

filename = "tekst.txt"

with open(filename) as f:
    content = f.read()
    print(content)
    # może być w jednym poleceniu: print(f.read())

print("Koniec")

