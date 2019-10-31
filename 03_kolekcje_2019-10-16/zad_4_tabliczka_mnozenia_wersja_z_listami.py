"""
Utwórz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.
"""

vector = []
for i in range(1, 11):
    vector.append(i)

matrix = []
for i in range(1, 11):
    matrix.append(vector)

for i in range(1, 11):
    print()
    for j in range(1, 11):
        matrix[i - 1][j - 1] = i * j
        if i*j <10:
            print("  " + str(matrix[i-1][j-1]), end=" ")
        elif i*j < 100:
            print(" " + str(matrix[i-1][j-1]), end=" ")
        else:
            print(str(matrix[i-1][j-1]), end=" ")
print()



