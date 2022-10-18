from itertools import *
count = 0

for a in product('WASD', repeat=5):
    st = ''.join(a)
    if (st[0] != 'W') and (st != st[::-1]):
        count += 1
print(count)