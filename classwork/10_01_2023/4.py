from functools import lru_cache
from sys import *
ans = set()
setrecursionlimit(100000000)


def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        ans.add(count)
        return 1
    else:
        return f(start + 1, end, count + 1) + f(start * 2, end, count + 1) + f(start * 3, end, count + 1)
print(f(1, 32718, 0))