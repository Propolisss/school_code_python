from functools import *

@lru_cache(None)
def f(n):
    if n <= 1:
        return 0
    elif n > 1 and (n & 1):
        return (n + 1) // 2 + f(n - 1)
    else:
        return 2 * f(n - 1) + 1
print(f(33))