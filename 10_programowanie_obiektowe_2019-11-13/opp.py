import random

class Dog:
    tail = True

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.pseudo = name + "-" + "color"

    def pseudo(self):
        adj = ["destroyer", "powerful", "funny", "sweet"]
        return self.name + "-" + random.choice(adj)

    def bark(self):
        return "hau" * self.age

obj_pimpek = Dog("Pimpek", "Collie", 5, "white")

print(obj_pimpek.name)
print(obj_pimpek.breed)
print(obj_pimpek.age)
print(obj_pimpek.color)

obj_dyzio = Dog("Dyzio", "Cotton de tulear", 7, "blond")

print(obj_pimpek.tail)
print(obj_dyzio.tail)
print(Dog.tail)

print(Dog.__dict__)
print(obj_dyzio.__dict__)

print(Dog.pseudo(obj_dyzio))

names = "Anna, Marta, Marek, Paweł"
print(names.split(","))
print(type(names))

print(str.split(names, ","))

print(obj_dyzio.bark())
