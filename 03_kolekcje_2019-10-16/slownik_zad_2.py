"""
Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2-elementowe.
Przekształć ją w słownik dict_from_tuples.
"""

tuples_to_dict = (
    ("apple", "jabłko"),
    ("pear", "gruszka"),
    ("cherry", "wiśnia"),
    ("strawberry", "truskawka")
)

print()
print(tuples_to_dict)
print(type(tuples_to_dict))
print(tuples_to_dict[0])
print(tuples_to_dict[0][0])
print(tuples_to_dict[0][1])

dict_from_tuples = dict(tuples_to_dict)

print()
print(dict_from_tuples)
print(type(dict_from_tuples))
print(dict_from_tuples['apple'])

