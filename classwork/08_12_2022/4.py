

def f(n):
    if n < 2:
        return 1
    elif n >= 2 and (n % 3 == 0):
        return f(n / 3) - 1
    elif n >= 2 and (n % 3 != 0):
        return f(n - 1) + 7

for i in range(1, 100_000):
    if f(i) == 111:
        print(i)
        break