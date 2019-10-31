"""
Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c).
"""


def maximum_of(a, b, c):

    maximum = (a if a >= b else b)
    Max = maximum if maximum >= c else c

    return Max


x = 1
y = 2
z = 3

print(maximum_of(x, y, z))
