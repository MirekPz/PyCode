"""
Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
    Dorota, Wellman, dziennikarka
    Adam, Małysz, skoczek
    Robert, Lewandowski, piłkarz
    Krystyna, Janda, aktorka
Wyświetl w sposób przyjazny dla użytkownika
"""

tablica = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "skoczek"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]
for i in range(4):
    for j in range(3):
        print(tablica[i][j], end=" ")
    print()
