"""
Stwórz własną implementację kolejki FIFO.
Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
Wśród metod powinny się znaleźć takie jak: wyświetlenie kolejki, sprawdzenie czy jest pusta,
dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
Utwórz kilka obiektów klasy Queue z różnymi parametrami.
"""

class Fifo:

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return "-".join(self.elements)

    def show(self):
        print(self.elements)

    def get(self):
        if len(self.elements) == 0:
            return "--- Brak elementów do zdjęcia z listy kolejkowej!"
        return self.elements.pop(0)

    def put(self, value):
        self.elements.append(value)
        return "Dodano element do kolejki"


list_elem = ["a", "b", "c", "d"]
fifo1 = Fifo(list_elem)

print("Początkowy stan kolejki:", fifo1)
fifo1.show()
print("Zdejmowany jest element:", fifo1.get())
print("Bieżący stan kolejki:", fifo1)
print("Zdejmowany jest element:", fifo1.get())
print("Bieżący stan kolejki:", fifo1)
print("Zdejmowany jest element:", fifo1.get())
print("Bieżący stan kolejki:", fifo1)
print("Zdejmowany jest element:", fifo1.get())
print("Bieżący stan kolejki:", fifo1)
print("Zdejmowany jest element:", fifo1.get())
v = input("Podaj element: ")
fifo1.put(v)
print(fifo1)
