"""
Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
"""

txt = input("Podaj wyraz o długości nieparzystej większej od 7: ")
srodek = len(txt)//2
new_txt = txt[srodek-1:srodek+2]
print(new_txt)
