"""
Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
"""


class Zwierzeta:
    def __init__(self):
        print("<Zwierzęta> - to jest klasa nadrzędna dla wszystkich klas.")


class Ssaki(Zwierzeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_super_desc(self):
        super().__init__()

    def show_description(self):
        print("Ssaki (Mammalia) – zwierzęta należące do kręgowców, charakteryzujące się głównie ",
              "występowaniem gruczołów mlekowych u samic")


class Kot(Ssaki):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Pies(Ssaki):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_description(self):
        print("Jestem psem.")


class Czlowiek(Ssaki):
    def __init__(self, name, age):
        self.name = name
        self.age = age


obiekt = Ssaki('Mruczek', 2)
obiekt.show_super_desc()
print(obiekt.name, obiekt.age)
obiekt.show_description()
obiekt = Pies('Aza', 10)
print(obiekt.name, obiekt.age)
obiekt.show_description()