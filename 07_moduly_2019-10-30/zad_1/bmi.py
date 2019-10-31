def calc_bmi(weight, height):
    bmi = weight/height**2
    return round(bmi, 2)


def bmi_status(bmi):
    if bmi < 19:
        return 'Niedowaga'
    elif bmi < 25:
        return "Waga normalna"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"


def main():
    print("********")
    result = calc_bmi(60, 1.80)
    print("********")


if __name__ == '__main__':
    main()

