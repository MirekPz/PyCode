print("I'm module")

print('__name__ value:', __name__)


# ====

# test.py
print('Testowy moduł')

if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
else:
    print('Plik zaimportowano jako moduł')
