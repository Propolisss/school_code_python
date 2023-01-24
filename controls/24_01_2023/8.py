from itertools import *

s = set(map(''.join, permutations('АМФИБРАХИЙ')))

count = 0

for i in s:
    if i[4:6] == 'БР':
        count += 1
print(count)