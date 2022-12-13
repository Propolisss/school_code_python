from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 3:
        return n
    elif n > 3:
        if (n & 1):
            return 2 * n + f(n - 2)
        else:
            return n * n + f(n - 1)
print(f(500) - f(495))

z = (10000 ** 2) + 9999 * 2 + 9997 * 2
zz = 0
for i in range(9995, 0, -2):
    if i <= 3:
        zz += i
    else:
        zz += i * 2

print((zz + z) - zz)