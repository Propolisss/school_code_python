from itertools import *

s = list(map(''.join, permutations('СПОРТЛОТО')))

ss = set()

for i in range(len(s)):
    if s[i][0] != 'О' and s[i][-1] != 'О':
        ss.add(s[i])
print(len(ss))