"""
Oblicz średnią arytmetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinien być odporny na błędy użytkownika.
Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
"""

# numbers = []
# while number != "Q" and number != "q":
#     number = input("Podaj kilka liczb oddzielonych przecinkiem, do wyliczenia średniej  (zakończ klawiszem Q): ")
#     numbers.append(number)
#
# print(numbers)

try:
    numbers = input("Podaj kilka liczb całkowitych oddzielonych przecinkiem, do wyliczenia średniej: ")
except Exception as ex:
    # with open("errors.txt"):
    print(ex)

numbers_list = numbers.split(',')
print(numbers_list)

# sum = 0
# for element in range(len(numbers_list)):
#     numbers_list[element] = int(numbers_list[element])
#     sum = sum + numbers_list[element]
# print(numbers_list)
# print(sum)
# average = sum / len(numbers_list)
# print(average)

list_exc = []
for index, element in enumerate(numbers_list):
    try:
        numbers_list[index] = float(element)
    except (ValueError, TypeError) as exc:
        # print(exc)
        list_exc.append(exc)
        numbers_list[index] = "-"

while '-' in numbers_list:
    numbers_list.remove('-')

print(numbers_list)
avg = sum(numbers_list)/len(numbers_list)
print(avg)
print(list_exc)

with open("errors.txt", "w") as f:
    for i in list_exc:
        f.write(str(i) + "\n")

