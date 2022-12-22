from itertools import *

def simple(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

for i in range(1_411_111_115, 1_411_111_127 + 1):
    if '0' in str(i):
        continue
    s = set(map(''.join, permutations(str(i))))
    for num in s:
        if simple(int(num)):
            print(i)
            break