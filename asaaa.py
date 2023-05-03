from itertools import product
from random import randint
letters = 'XYZ'

def f1(st):
    #file = open('11').readline()
    file = st
    lett = '123'
    maax = 0
    all = []
    for i in range(1, 7):
        comb = list(map(''.join, product(lett, repeat = i)))
        comb = [x for x in comb if x == x[::-1]]
        for item in comb:
            st = file.split(item)
            for x in st:
                if (item + x + item) == (item + x + item)[::-1] and (item + x + item) in file:
                    maax = max(maax, len(x) + i * 2)
                    #all.append(item + x + item)
    return (maax)
    #print(sorted(all, key = len, reverse = True)[:50])

def f2(st):
    #st = open('24_1761.txt').readline()
    maxx = 1
    maxx_pal = ''

    for i in range(1, len(st) - 1):
        curr_1 = 1
        curr_0 = 2
        if st[i] == st[i + 1]:
            maxx = max(maxx, curr_0)
            for j in range(1, i + 1):
                    if i + j + 1 < len(st) and st[i - j] == st[i + j + 1]:
                        curr_0 += 2
                        maxx = max(maxx, curr_0)
                    else:
                        break
        for j in range(1, i + 1):
                if i + j < len(st) and st[i - j] == st[i + j]:
                    curr_1 += 2
                    maxx = max(maxx, curr_1)
                else:
                    break
    return (maxx)


def f3(st):
    maxx = float('-inf')

    for i in range(len(st)):
        temp = ''
        for j in range(i, len(st)):
            temp += st[j]
            if temp == temp[::-1]:
                maxx = max(maxx, len(temp))
    return maxx

while True:
    stt = ''.join([letters[randint(0, 2)] for i in range(1_000)])
    res1 = f1(stt)
    res2 = f2(stt)
    res3 = f3(stt)
    print(res1, res2, res3, (res1 + res2 + res3) == 3, res2 == res3)