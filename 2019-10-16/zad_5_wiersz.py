"""
W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
    Szybko, zbudź się, szybko, wstawaj
    Szybko, szybko, stygnie kawa
    Szybko, zęby myj i ręce
Zadbaj o sposób wyświetlania np.:
    szybko : 5
    zbudź : 1
"""

poem = """Szybko, zbudź się, szybko, wstawaj 
    Szybko, szybko, stygnie kawa 
    Szybko, zęby myj i ręce """

poem = poem.replace(",", "").lower()

words = poem.split()

occurrence = {}

for word in words:
    if word not in occurrence:
        occurrence[word] = 1
    else:
        occurrence[word] += 1

print()
for element1, element2 in occurrence.items():
    print(element1, ":", element2)



