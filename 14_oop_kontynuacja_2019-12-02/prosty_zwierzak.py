class Critter:  # klasa jest typem  (critter [en] = stwór [pl])

    def __init__(self, name):
        self.name = name
        print("Urodził się nowy zwierzak")  # konstruktor --> metoda wywoływana zaraz po utworzeniu nowego obiektu
                                            # metoda inicjalizacji
    def talk(self):
        print("Cześć! Jestem egzemplarzem klasy Critter.")
        print(f"Moje imie to {self.name}")


obiekt1_nowy_zwierzak = Critter("reksio")
obiekt1_nowy_zwierzak.talk()

obiekt2 = Critter("dyzio")
obiekt3 = Critter("aza")

obiekt2.talk()
obiekt3.talk()

print(type(obiekt2))
