"""
Utwórz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.
"""

for row in range(1, 11):
    for col in range(1, 11):
        if row*col < 10:
            print("  " + str(row*col), end=" ")
        elif row*col < 100:
            print(" " + str(row*col), end=" ")
        else:
            print(str(row*col), end=" ")
    print()
