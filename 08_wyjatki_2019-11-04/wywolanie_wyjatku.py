import sys

def hello_exception():
    print("Początek programu")
    raise ArithmeticError("To jest błąd arytmetyczny")
    print("Koniec programu")

#hello_exception()


try:
    hello_exception()
except ArithmeticError as ex:
    print("Oh, nie. Błąd", ex)
    print(sys.exc_info())
except:
    print("Inny błąd")
