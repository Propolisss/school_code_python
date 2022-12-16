from functools import lru_cache
from itertools import *


@lru_cache(None)
def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

ans = set()

for i in range(1_411_111_115, 1_411_111_127 + 1):
    if '0' in str(i):
        continue
    s = set(map(''.join, permutations(str(i), 10)))
    for j in s:
        if simple(int(j)):
            print(i)
            break