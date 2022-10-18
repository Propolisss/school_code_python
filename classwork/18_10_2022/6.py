from itertools import *

count = 0

for st in permutations('СОТКАПЛЗ', 5):
    st = ''.join(st)
    if (st[-1] not in 'ОА') and 'ЗЛО' not in st:
        count += 1
print(count)