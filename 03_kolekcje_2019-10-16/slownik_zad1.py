"""
Utwórz listę lists_to_dict zawierającą listy 2-elementowe.
Przekształć ją w słownik dict_from_list.
"""

list_to_dict = [
    ["apple", "jabłko"],
    ["pear", "gruszka"],
    ["cherry", "wiśnie"]
]

dict_from_list = dict(list_to_dict)

print(dict_from_list)
print(dict_from_list["apple"])

print(list_to_dict[0][1])

