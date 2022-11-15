from functools import *


@cache
def f(n):
    if n < 3:
        return n + 1
    elif n >= 3 and n % 2 == 0:
        return f(n - 2) + n - 2
    elif n >= 3 and n & 1:
        return f(n + 2) + n + 2

count = 0

for i in range(1, 10000):
    try:
        if 10000 <= f(i) <= 99999:
            count += 1
    except:
        continue
print(count)