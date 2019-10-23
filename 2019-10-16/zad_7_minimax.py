"""
7▹ Usuń duplikat z podanej listy i utwórz na jej bazie krotkę.
Znajdź minimalną i maksymalną liczbę w krotce.
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
"""

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
krotka = tuple(set(example_list))

print()
print("Krotka:\t", krotka)
print("Wartość minimalna:\t", min(krotka))
print("Wartość maksymalna:\t", max(krotka))
