import figures
import test

def main():
    print("Pole trójkąta: ", figures.triangle_field(1, 2))
    print("Pole kwadratu: ", figures.square_field(2))
    print("Pole koła: ", figures.circle_field(1))
    print("Pole trapezu: ", figures.trapeze_field(2, 3, 4))


print(__name__)

if __name__ == '__main__':
    main()
