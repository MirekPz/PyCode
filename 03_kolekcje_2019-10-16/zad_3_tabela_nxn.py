"""
Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
Elementy powinny być oddzielone spacją
    wejście:
n = 3
tab = [['-', '-', '-']
       ['-', '-', '-'],
        ['-', '-', '-']]
wyjście:
- - -
- - -
- - -
"""

n = int(input("\nPodaj rozmiar tablicy kwadratowej: "))

znak = '-'
tab = [[znak] * n] * n

print("\nTablica n x n:")
print(tab)

print("\nTabela złożona z list:")
for i in range(n):
    print(tab[i])

print("\nTabela złożona z samych znaków:")
for i in range(n):
    for j in range(n):
        print(tab[i][j], end=" ")
    print()
