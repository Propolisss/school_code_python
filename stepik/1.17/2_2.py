from itertools import *


def len_n(n):
    s = set(map(''.join, permutations(str(n), 2)))
    return len(s)

maxx = float('-inf')
for i in range(1000, 9999 + 1):
    maxx = max(maxx, len_n(i))

minn_n = float('inf')
maxx_n = float('-inf')

for i in range(1000, 9999 + 1):
    if len_n(i) == maxx:
        print(i)
        minn_n = min(minn_n, i)
        maxx_n = max(maxx_n, i)
print(maxx_n - minn_n)