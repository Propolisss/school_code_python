from itertools import *
count = 0
counter = 0
for st in permutations('ЗАПИСЬ'):
    st = ''.join(st)
    count = 0
    flag = 1
    if (st[0] != 'Ь'):
        count += 1
    if ('АЬ' in st) or ('ИЬ' in st):
        flag = 0
    if count and flag:
        counter += 1
print(counter)