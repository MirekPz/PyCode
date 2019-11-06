"""
Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""


def suma_while(n):
    s=0
    while n>0:
         s = s+n
         n = n-1
    return s


print("Suma while: ", suma_while(10))


def suma_recursion(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursion(n-1)


print("Suma rekurencyjnie: ", suma_recursion(10))
