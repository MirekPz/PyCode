class Liczba_zespolona:
    def __init__(self, rzeczywista, urojona):
        self.rzeczywista = rzeczywista
        self.urojona = urojona

    def __add__(self, l):
        czesc_rzeczywista = self.rzeczywista + l.rzeczywista
        czesc_urojona = self.urojona + l.urojona
        return (Liczba_zespolona(czesc_rzeczywista, czesc_urojona))

    def __sub__(self, l):
        czesc_rzeczywista = self.rzeczywista - l.rzeczywista
        czesc_urojona = self.urojona - l.urojona
        return (Liczba_zespolona(czesc_rzeczywista, czesc_urojona))

    def rzeczywista():
        return self.rzeczywista

    def urojona():
        return self.urojona

    def __str__(self):
        return "{} + {}i".format(self.rzeczywista, self.urojona)


x = Liczba_zespolona(2, 4)
y = Liczba_zespolona(3, 1)
print(x + y)
print(x - y)
