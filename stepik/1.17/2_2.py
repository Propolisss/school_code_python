from itertools import *

maxx = float('-inf')
ans = []

for i in range(1023, 9999 + 1):
    s = set(map(''.join, permutations(str(i), 2)))
    s = list(s)
    count = 0
    for j in range(len(s)):
        if int(s[j]) >= 10:
            count += 1
    maxx = max(maxx, count)

for i in range(1000, 9999 + 1):
    s = set(map(''.join, permutations(str(i), 2)))
    s = list(s)
    count = 0
    for j in range(len(s)):
        if int(s[j]) >= 10:
            count += 1
    if count == maxx:
        ans.append(i)

print(max(ans) - min(ans))