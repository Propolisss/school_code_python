from functools import lru_cache
from sys import *
ans = set()
setrecursionlimit(100000000)

@lru_cache(None)
def f(start, end, count):
    if start > end or count > 20:
        return 0
    elif start == end:
        ans.add(count)
        return 1
    else:
        return f(start + 1, end, count + 1) + f(start * 2, end, count + 1) + f(start * 3, end, count + 1)
f(1, 32718, 0)
print(min(ans))