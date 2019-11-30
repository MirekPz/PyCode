"""
Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zwracającą
łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
    Utwórz funkcję zwracającą tekst
    Utwórz dekorator przyjujący tę funkcję
    Wywołaj funkcję, by sprawdzić, że decorator działa
"""

# @uppercase_decorator

def text_decorator():

    def func_text():
        return "Zwracany tekst"

    return func_text

upper_text = text_decorator()
upper_text()
print(upper_text().upper())
