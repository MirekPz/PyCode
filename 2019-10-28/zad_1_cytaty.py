"""
 Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinien się znaleźć w nowej linii.
 Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:

Quote of the day is:

**************************************
           be or not to be?
**************************************

    zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami

    plik z cytatami powinien również zawierać informację o autorze, wyświetl cytat i pod spodem autora
"""

import random

filename = input("Wybierz plik z cytatami: ")

with open(filename, encoding="UTF-8") as file:
    list_of_quotations = file.readlines()

# print(list_of_quotations)

"""
for i in list_of_quotations:
    print(i.strip())
"""

print("\nQuote of the day is:")
print("*" * 150)
quote_for_today = random.choice(list_of_quotations)
with_author = quote_for_today.split(":")
print(with_author[0].center(150))
print(with_author[1].strip().center(150))
print("*" * 150)

