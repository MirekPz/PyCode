is_number = False
while not is_number:
    partner_id = input("Podaj ID partnera: ")
    try:
        int_partner_id = int(partner_id)  # potrzebne tylko dla sprawdzenia czy indeks jest liczbą
        is_number = True
    except ValueError:
        print("\nIndeks musi być liczbą naturalną! Popraw wpisywane dane.")

"""
Wyświetlenie strony głównej:
input: https://helion.pl/ ; input: numer partnera - 90412 ; output: https://helion.pl/view/90412
"""

main_url = "https://helion.pl/"
output_url = main_url + "view/" + partner_id
print("\nStrona główna:")
print(output_url + "\n")

"""
Wyświetlenie strony produktu:
input: https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d
output: https://helion.pl/view/90412/algoip
"""

title_url = input("Przekopiuj tu link z tytułem książki, dodaj spacje na końcu: \n")

# usuwanie z linka wszystkiego co jest przed przecinkiem:
# print(title_url[title_url.index(","):])
title_symbol = title_url[title_url.index(","):]

# bez początkowego przecinka i do pierwszego wystąpienia kropki w dalszej części linka:
title_symbol = title_symbol[1:title_symbol.index(".")]
# print(title_symbol)

output_url = "https://helion.pl/view/" + partner_id + "/" + title_symbol
print("Link partnerski do wybranej książki: " + output_url)

"""
Wyświetlenie strony promocji:
input: https://helion.pl/kategorie/promocja-2za1
output: https://helion.pl/page/90412/promocja/promocja-2za1
"""
