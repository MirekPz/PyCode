"""
Policz elementy na liście, dopóki element nie będzie krotką.
"""

numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
    print(numbers[counter])
    if isinstance(n, tuple):
        break
    counter = counter + 1
print("Wynik: ", counter)
