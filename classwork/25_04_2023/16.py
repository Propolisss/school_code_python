def f(n):
    if n == 1:
        return 1
    elif n > 1 and (n % 2 != 0):
        return 3 * n + f(n - 2)
    elif n > 1 and (n % 2 == 0):
        return 4 * f(n // 2)
print(f(42))