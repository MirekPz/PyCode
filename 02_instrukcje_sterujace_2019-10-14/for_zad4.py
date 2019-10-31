"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).
"""

N = int(input("Podaj liczbę naturalną nie większą niż 8: "))

silnia = 1
for n in range(1, N + 1):
    silnia = silnia * n
    print(str(n)+"! = ", silnia)
