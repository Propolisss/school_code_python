from itertools import *

def f(x):
    P = 1 <= x <= 40
    Q = 25 <= x <= 120
    A = a1 <= x <= a2
    return Q <= (((not P) and Q) <= A)

ox = [i / 4 for i in range(0 * 4, 121 * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lens.append(abs(a2 - a1))
print(round(min(lens)))