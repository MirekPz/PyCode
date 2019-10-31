"""
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
np.: Kobyła ma mały bok.
Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
"""

palindrom = input("Wprowadź dowolne zdanie: ")

palindrom = palindrom.replace(".", "")
palindrom = palindrom.replace(" ", "")

print(palindrom.lower() == palindrom[::-1].lower())
