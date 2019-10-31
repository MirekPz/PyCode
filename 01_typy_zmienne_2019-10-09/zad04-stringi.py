# jak sprawdzić czy ciąg znaków sklada się tylko z cyfr?
# https://docs.python.org/3/library/stdtypes.html#string-methods

string = input("Podaj ciąg znaków: ")
print(string.isdecimal())               # wynik: True lub False

#============

print(string.center(20))
print(string.center(20, '*'))

#============

print(string.rstrip('12345'))

#==============

print(not string.islower())

print(string.isalpha() and not string.islower())

#------

print(string.count('na'))
