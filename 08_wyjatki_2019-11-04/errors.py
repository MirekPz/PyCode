x = int(input("Podaj liczbę: "))

error = False

# try:
#     print(1/x)
# except ZeroDivisionError as e:
#     print("Dzielenie przez zero! \nWystąpił wyjątek: ", e)
#     print(ZeroDivisionError.__bases__)
#     error = True

# try:
#     print(1/x)
# except Exception as e:
#     print("Exception: ", e)
#     error = True


# try:
#     print(1/x)
# except ZeroDivisionError as e:
#     print("\nDzielenie przez zero! \nWystąpił wyjątek: ", e)
#     error = True
# finally:
#     print("\nZawsze sie wyświetlę")


import sys
try:
    print(1/x)
except Exception as err:
    print(err)
    print("Blad to: ", sys.exc_info())
    print("Blad to: ", sys.exc_info()[1])
    error = True


if not error:
    print(x, "====> ", 1/x)
