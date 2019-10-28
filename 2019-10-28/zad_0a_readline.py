with open('tekst.txt', 'r') as fopen:

    while True:
        current_line = fopen.readline()

        if current_line == '':      # aktualna linia jest pusta
            # dotarliśmy do końca
            break
        print(current_line)
