from itertools import *

count = 0
ref = 'ШАРЛАТАН'
s = set()

for st in permutations('ШАРЛАТАН'):
    st = ''.join(st)
    flag2 = 0
    for i in range(1, len(st)):
        if (st[i - 1] in 'ШРЛТН' and st[i] in 'ШРЛТН') or (st[i - 1] in 'А' and st[i] in 'А'):
            flag2 = 1
    if flag2:
        s.add(st)
print(len(s))
