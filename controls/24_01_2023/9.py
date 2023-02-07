from itertools import *

def f(x, y, w, z):
    return (not(z <= x)) or (y == w) or w

for a in product([0, 1], repeat=6):
    table = [(0, 0, a[0], a[1]), (0, a[2], a[3], a[4]), (0, 1, a[5], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(*p, sep='')