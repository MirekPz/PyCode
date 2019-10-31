# Rozwiązanie Rity

names = input("Podaj kilka imion podzielone spacją: ")
print(names)
names = names.split()
print(names)

for name in names:
    print("Hello ", name, "!")

print("---------------")

id = 0
while id < len(names):
    print("Hi", names[id])
    id = id + 1

