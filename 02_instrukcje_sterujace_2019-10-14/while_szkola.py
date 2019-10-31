i = 0
dict = {}

while i < 3:
    subject = input("Podaj nazwę przedmiotu w szkole: ")
    grade = input("Ocena w skali 1-6: ")
    dict[subject] = grade
    i = i + 1

print(dict)
