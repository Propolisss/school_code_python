from itertools import *
gl = 'АИУОЯ'
sogl = 'НТП'

def check_gl(st):
    temp_st = ''

    for i in st:
        if i in gl:
            temp_st += i
    return all(temp_st[i - 1] >= temp_st[i] for i in range(1, len(temp_st)))

def check_sogl(st):
    temp_st = ''
    if sum(1 if j in sogl else 0 for j in st) in [0, 1]: return True
    if sum(1 if j in sogl else 0 for j in st) <= 2:
        for i in st:
            if i in sogl:
                temp_st += i
        return all(temp_st[i - 1] <= temp_st[i] for i in range(1, len(temp_st)))
    return False

s = list(map(''.join, product('АНТИУТОПИЯ', repeat=6)))
ans = set()

for i in s:
    if check_gl(i) and check_sogl(i):
        print(i)
        ans.add(i)
print(len(ans))