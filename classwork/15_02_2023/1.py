from itertools import *

def f(x):
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    a = a1 <= x <= a2
    f1 = P <= a
    f2 = (not a) <= (not Q)
    if f1 and f2:
        return 1
    return 0

ox = [i / 4 for i in range(34 * 4, (65 + 1) * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lens.append(abs(a2 - a1))
print(min(lens))