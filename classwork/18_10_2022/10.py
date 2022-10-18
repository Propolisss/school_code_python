from itertools import *

s1 = list(map(''.join, permutations('МАРИ')))
s2 = list(map(''.join, product('ИНА', repeat=4)))

s = []

for i in s1:
    for j in s2:
        s.append(i + j)
s.sort()
print(s.index('МАРИАННА') + 1)