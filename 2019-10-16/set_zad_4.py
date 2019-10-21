"""
Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
    input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
    output:
    [4, 3, 2, 1]
    [14, 13, 12, 11]
    [24, 23, 22, 21]
"""
long_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

list1 = long_list[0:int(len(long_list)/3)]
list2 = long_list[len(list1):2*len(list1)]
list3 = long_list[2*len(list1):]

list1.reverse()
list2.reverse()
list3.reverse()

print(list1)
print(list2)
print(list3)
