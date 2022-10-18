from functools import lru_cache

s = 'CONST'

@lru_cache
def f(st):
    if len(st) == 16:
        if st[-1] == 'S':
            return 0
        return 1
    else:
        a = 0
        for i in s:
            if st[-1] != i:
                if st[-1] == 'S' and st[-2] == i:
                    a += 0
                else:
                    a += f(st + i)
        return a



print(f('C') + f('O') + f('N') + f('T'))