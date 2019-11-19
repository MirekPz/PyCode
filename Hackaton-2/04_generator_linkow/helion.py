is_number = False
while not is_number:
    partner_id = input("Podaj ID partnera: ")
    try:
        int_partner_id = int(partner_id)  # potrzebne tylko dla sprawdzenia czy indeks jest liczbą
        is_number = True
    except ValueError:
        print("\nIndeks musi być liczbą naturalną! Popraw wpisywane dane.")

"""
rozpoznawanie rodzaju strony na podstawie podanego linku:
1.strona główna       https://helion.pl/
2.tytuł książki  np.  https://helion.pl/ksiazki/python-wprowadzenie-wydanie-iv-mark-lutz,pytho4.htm#format/d
3.kategoria      np.  https://helion.pl/kategorie/elektronika
"""

url = input("Przekopiuj tu link z tytułem książki lub kategorii, dodaj spację na końcu: ")

# jeżeli w nazwie mamy przecinek, to link prowadzi do tytułu konkretnej książki,
# w przeciwnym wypadku do kategorii lub strony głównej Helionu
# funkcja find() zwraca -1 jeżeli szukany ciąg nie znajduje się w napisie

comma_position = url.find(",")
# print(comma_position)

if comma_position > -1:
    # link jest tytułem książki

    # usuwanie z linka wszystkiego co jest przed przecinkiem:
    # print(url[url.index(","):])
    title_symbol = url[url.index(","):]

    # bez początkowego przecinka i do pierwszego wystąpienia kropki w dalszej części linka:
    title_symbol = title_symbol[1:title_symbol.index(".")]
    # print(title_symbol)

    output_url = "https://helion.pl/view/" + partner_id + "/" + title_symbol
    print("Link partnerski do wybranej książki: " + output_url)

else:
    if url.strip().lower() == "https://helion.pl/" or url.strip().lower() == "helion.pl":
        """
            Wyświetlenie strony głównej:
            input: https://helion.pl/
            input: numer partnera - 90412
            output: https://helion.pl/view/90412
        """
        main_url = "https://helion.pl/"
        output_url = main_url + "view/" + partner_id
        print("\nStrona główna:")
        print(output_url + "\n")
    else:
        # strona kategorii
        pass




"""
Wyświetlenie strony produktu:
input: https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d
output: https://helion.pl/view/90412/algoip
"""




"""
Wyświetlenie linku do kategorii:
wzór: https://helion.pl/page/id/kategorie/link_do_kategorii
input: https://helion.pl/kategorie/programowanie
output: https://helion.pl/page/90412/kategorie/programowanie
"""

#  ?????????/
#  category_url = input("Przekopiuj tu link z tytułem kategorii, dodaj spacje na końcu: \n")

