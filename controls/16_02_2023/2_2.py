from itertools import *

def f(x):
    P = 25 <= x <= 37
    Q = 32 <= x <= 47
    A = a1 <= x <= a2
    return (A and (not P)) <= ((not P) and Q)

ox = [i / 4 for i in range(24 * 4, (47 + 1) * 4)]
m = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(abs(a2 - a1))
print(max(m))