"""
Wyświetl tylko 5 pierwszych linii
"""

filename = "cytaty.txt"

with open(filename, encoding="UTF-8") as file:
    for i in range(5):
        list_of_quotations = file.readline()
        print(list_of_quotations)

