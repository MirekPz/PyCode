n = int(input("Podaj, który wyraz ciągu Fibonacciego należy wyliczyć: "))

f = []
for i in range(n):
    f.append(0)

f[0] = 0
f[1] = 1

i = 2
suma = 1
while i < n:
    f[i] = f[i-1] + f[i-2]
    suma = suma + f[i]
    i += 1

print(f)
print(f"{n} wyraz ciągu to: {f[n-1]}")
print(f"Suma pierwszych {n} wyrazów ciągu: {suma}")
