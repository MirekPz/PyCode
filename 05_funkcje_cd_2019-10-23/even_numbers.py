# Wypisać, które liczby z podanej listy są parzyste


def which_even(list_numbers):
    return [x for x in list_numbers if x % 2 == 0]


number_list = list(range(1, 11))
print(number_list)

print(which_even(number_list))
