class Pies:
    def __init__(self, imie, kolor, siersc, rasa):
        self.imie = imie
        self.kolor = kolor
        self.siersc = siersc
        self.rasa = rasa


obj_aza = Pies("Aza", "czarny", "długa", "owczarek")
print(obj_aza.imie)
print(obj_aza.kolor)
print(obj_aza.siersc)
print(obj_aza.rasa)
