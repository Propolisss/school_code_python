from itertools import *

def f(x, y, z, w):
    return (x or y) and (not(y == z)) and (not w)

for a in product([0, 1], repeat=4):
    table = [(1, a[0], 1, a[1]), (0, 1, a[2], 0), (a[3], 1, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p, sep='')