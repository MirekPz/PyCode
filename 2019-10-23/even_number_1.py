def is_even(number):
    if number % 2 == 0:
        return "liczba parzysta"
    else:
        return "liczba nieparzysta"


print(4, is_even(4))
print(7, is_even(7))
