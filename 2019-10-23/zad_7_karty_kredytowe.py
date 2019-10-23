"""
Napisz program, który na podstawie numeru karty odpowie czy ma do czynienia z Visą, MasterCard,
a może AmericanExpress.
Co wiemy o numerach tych kart?
- All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
- MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
  All have 16 digits.
- American Express card numbers start with 34 or 37 and have 15 digits.
"""

card_number = input("Put your card number here: ")

can_be_card_number = False

if len(card_number) < 13 or len(card_number) > 16:
    print("Wrong number")
else:
    if card_number.isdecimal():
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")

# Visa
if can_be_card_number and (len(card_number) == 16 or len(card_number) == 13):
    if card_number[0] == '4':
        print("Your card is Visa.")

# Mastercard
if can_be_card_number and len(card_number) == 16:
    if (int(card_number[0:2]) in range(51, 56)) or (int(card_number[0:4]) in range(2221, 2721)):
        print("Mastercard.")

# American Express
if can_be_card_number and len(card_number) == 15:
    if card_number[0:2] in ('34', '37'):
        print("America Express")
