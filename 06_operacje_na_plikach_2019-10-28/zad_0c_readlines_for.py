filename = "tekst.txt"

with open(filename, encoding="UTF-8") as fopen:
    list_of_lines = fopen.readlines()

print(list_of_lines)
print()
for i in list_of_lines:
    print("Linia: ", i.strip())     # strip() - usunięcie Entera na końcu wiersza
