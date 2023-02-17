from itertools import *
ans = []

def f(x):
    p = 10 <= x <= 20
    q = 35 <= x <= 45
    a = a1 <= x <= a2
    return ((not(p)) <= q) and (not(a))

ox = [x / 4 for x in range(9 * 4, 46 * 4)]

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 0 for x in ox):
        ans.append(abs(a1 - a2))

print(min(ans))
