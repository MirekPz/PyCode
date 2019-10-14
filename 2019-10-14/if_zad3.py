opinia1 = int(input("Opinia 1: "))
opinia2 = int(input("Opinia 2: "))
opinia3 = int(input("Opinia 3: "))

średnia = (opinia1 + opinia2 + opinia3)/3
wynik = round(średnia, 2)
print(wynik)

if wynik > 7:
    print('Bardzo dobry')
elif wynik > 5:
    print('Przeciętny')
else:
    print('Nie jest wart uwagi')
