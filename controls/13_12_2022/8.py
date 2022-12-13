from itertools import *

s = list(map(''.join, product('КАНТ', repeat=6)))
count = 0

for i in range(len(s)):
    if s[i].count('К') == 2:
        count += 1
print(count)