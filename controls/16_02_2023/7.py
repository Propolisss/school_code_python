from itertools import *

def f(x):
    P = 10 <= x <= 20
    Q = 35 <= x <= 45
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)

ox = [i / 4 for i in range(9 * 4, (45 + 1) * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 0 for x in ox):
        lens.append(abs(a2 - a1))
print(min(lens))