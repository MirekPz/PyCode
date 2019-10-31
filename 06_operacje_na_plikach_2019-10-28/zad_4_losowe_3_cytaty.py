"""
Wyświetl 3 losowe cytaty
"""

import random


def losuj_cytat(filename):

    with open(filename, encoding="UTF-8") as file:
        list_of_quotations = file.readlines()

    quote_for_today = random.choice(list_of_quotations)
    with_author = quote_for_today.split(":")
    print("\nQuote of the day is:")
    print("*" * 100)
    print(with_author[0].center(100))
    print(with_author[1].strip().center(100))
    print("*" * 100)


for i in range(3):
    losuj_cytat("tekst.txt")




# print(list_of_quotations)

"""
for i in list_of_quotations:
    print(i.strip())
"""


