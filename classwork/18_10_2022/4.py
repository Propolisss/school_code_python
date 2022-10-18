from itertools import *

count = 0
flag = 0
flag2 = 0

for a in product('АМРТ', repeat=4):
    st = ''.join(a)
    if st == 'МАРТ':
        flag = 1
    if st == 'РАМТ':
        flag2 = 1
    if flag and not flag2:
        count += 1
print(count + 1)