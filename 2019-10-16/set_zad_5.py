"""
Porównaj zachowanie discard() vs remove() dla typu set.
"""

list1 = []
for i in range(10):
    list1.append(i)
set1 = set(list1)
print(set1)

set1.remove(5)
print(set1)

set1.discard(7)
print(set1)

# próba usunięcia elementu, który nie istnieje w zbiorze:

set1.discard(10)    # brak komunikatu o błędzie, przejście do następnej linii kodu
print(set1)

print("\n")
set1.remove(10)     # komunikat o błędzie i przerwanie programu, KeyError

