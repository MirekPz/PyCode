n = int(input("Wysokość choinki: "))
znak = '#'

i = 1
while i <= n:
    print((n-i)*" " + znak * (2*i-1))
    # dla zachowania symetrii długość w poziomie musi być nieparzysta
    i += 1
pieniek = " " * ((2*n - 1)//2) + znak
# skoro długość w poziomie jest nieparzysta, to środek zawsze będzie na pozycji parzystej
if n < 8:
    print(pieniek)
else:
    print(pieniek)
    print(pieniek)

