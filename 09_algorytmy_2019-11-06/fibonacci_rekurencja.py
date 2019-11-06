def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)


# Uwaga: pierwszy wyraz ciągu rozumiemy matematycznie, a nie informatycznie
print(fib(3))
print(fib(6))
print(fib(10))
