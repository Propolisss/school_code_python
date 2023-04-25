from functools import lru_cache


@lru_cache(None)
def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(600_000 + 1, 10_000_000):
    if i % 6 == 0 and simple(i - 1) and simple(i + 1):
        print(i - 1, i + 1)
        count += 1
    if count == 6:
        break