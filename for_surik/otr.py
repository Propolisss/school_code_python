from itertools import *
ans = []
def f(x):
    p = 25 <= x <= 37
    q = 32 <= x <= 47
    a = a1 <= x <= a2
    return (a and (not(p))) <= ((not(p)) and (q))
ox = [1 / 4 * x for x in range(24 * 4, 48 * 4)]

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        ans.append(abs(a1 - a2))
print(max(ans))

