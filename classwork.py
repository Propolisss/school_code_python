from sys import *
from functools import *
setrecursionlimit(100_000)

@lru_cache(1_000_000)
def f(n):
    if n == 0:
        return 6
    elif n > 0 and (n % 2 == 0):
        return 1 + f(n // 2)
    else:
        return f(n // 2)


count = 0

for i in range(1, 1_000_000_000 + 1):
    if i % 1_000_000 == 0:
        print(i, count)
    if f(i) == 9:
        count += 1
print(count)