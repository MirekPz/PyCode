import bmi


def advice(filename):
    with open(filename + ".txt") as f:
        content = f.read()
    print(content)


def main():
    print("Podaj wagę i wzrost pacjenta:")
    weight = float(input("- waga: "))
    height = float(input("- wzrost: "))
    bmi_result = bmi.calc_bmi(weight, height)
    bmi_stan = bmi.bmi_status(bmi_result)
    print("BMI staus:", bmi_stan)
    advice(bmi_stan)


if __name__ == '__main__':
    main()
