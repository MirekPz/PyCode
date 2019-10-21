"""
Skorzystaj ze swojego kodu bmi.py.
Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
w zależności od otrzymanego parametru.
"""


def calc_bmi(weight, height):
    bmi = weight/height**2
    return round(bmi, 2)

def bmi_status(bmi):
    if bmi < 19:
        print('Niedowaga')
    elif bmi < 25:
        print("Waga normalna")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")


h = 1.87
w = 85

BMI = calc_bmi(w, h)
print(BMI)
bmi_status(BMI)
