def fib(n):
    f = []
    for i in range(n):
        f.append(0)

    f[0] = 0
    f[1] = 1

    i = 2
    while i < n:
        f[i] = f[i - 1] + f[i - 2]
        i += 1

    return f[n-1]


print(fib(10))

