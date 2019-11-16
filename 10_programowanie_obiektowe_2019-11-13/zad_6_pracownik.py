"""
Utwórz klasę Pracownik.
    Pracownik ma stanowisko, wynagrodzenie, imię, nazwisko, staz pracy.
    Pracownik powinien mieć roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
    Pracownik powinien odprowadzać podatek o wysokości zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
    Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
    Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
    Wszyscy pracownicy mają wspólną nazwę firmy.
    Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy.
    np. Adam Kowalski Love Python Company
    email -> dmkwlsk@lovepythoncompany.com
"""


class Employee:

    company = "Love Python"

    def __init__(self, position, salary, name, surname, seniority, is_student):
        self.position  = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.is_student = is_student

    def salary_bump(self):   # podwyżka roczna
        self.salary *= 1.07
        return self.salary

    def tax(self):
        return self.salary * 0.02

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary * proc

    def employee_email(self):
        primary = self.name + "." + self.surname
        secondary = self.company.replace(" ", "").lower() + ".com"
        email = primary + "@" + secondary
        return email


p1 = Employee("programista", 5500, "Jan", "Kowalski", 3, False)
print(p1.name + " " + p1.surname)
print(p1.salary)
print(p1.tax())
print(p1.salary_bump())
print(p1.tax())
print(p1.company)
print(p1.employee_email())
