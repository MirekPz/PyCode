"""
Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c).
"""

def maximum_of(a, b, c):

    if a >= b:
        maximum = a
    else:
        maximum = b

    if maximum >= c:
        Max = maximum
    else:
        Max = c

    return Max


x = 3
y = 8
z = 2

print(maximum_of(x, y, z))
