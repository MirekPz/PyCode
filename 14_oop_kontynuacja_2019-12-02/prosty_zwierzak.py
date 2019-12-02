class Critter:  # klasa jest typem  (critter [en] = stwór [pl])

    total = 0

    def __init__(self, name):
        self.name = name
        print("\nUrodził się nowy zwierzak")  # konstruktor --> metoda wywoływana zaraz po utworzeniu nowego obiektu
                                            # metoda inicjalizacji
        Critter.total = Critter.total + 1
        print(Critter.total)

    def talk(self):
        print("Cześć! Jestem egzemplarzem klasy Critter.")
        print(f"Moje imie to {self.name}")


obiekt1_nowy_zwierzak = Critter("reksio")
obiekt1_nowy_zwierzak.talk()
print("obiekt1", obiekt1_nowy_zwierzak.total)
print('------------')

obiekt2 = Critter("dyzio")
obiekt2.talk()

obiekt3 = Critter("aza")
obiekt3.talk()

print('\n', type(obiekt2))
