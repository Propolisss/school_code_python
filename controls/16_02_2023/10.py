from itertools import *

def f(x):
    P = 254 <= x <= 800
    Q = 410 <= x <= 823
    A = a1 <= x <= a2
    return (P and (not A)) <= Q

ox = [i / 4 for i in range(253 * 4, 824 * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lens.append(abs(a2 - a1))
print(round(min(lens)))