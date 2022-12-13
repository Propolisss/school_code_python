from fnmatch import *

def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return dels_


for i in range(10 ** 7, 0, -1):
    if fnmatch(str(i), '9?*55*7'):
        dels = sum(div(i))
        print(i, dels % 21)