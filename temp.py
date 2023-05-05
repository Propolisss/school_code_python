from functools import lru_cache
from random import randint

def f1():
    @lru_cache(None)
    def find_road(n):
        if (n + 1) in dic and (n + 2) in dic:
            return max(find_road(n + 1), find_road(n + 2))
        elif (n + 1) in dic:
            return find_road(n + 1)
        elif (n + 2) in dic:
            return find_road(n + 2)
        else:
            return n
    @lru_cache(None)
    def find_summ(n, summ):
        if (n + 1) in dic and (n + 2) in dic:
            if dic[n][0] < dic[n][1]:
                return find_summ(n + 1, summ + dic[n][0])
            else:
                return find_summ(n + 2, summ + dic[n][1])
        elif (n + 1) in dic:
            return find_summ(n + 1, summ + dic[n][0])
        elif (n + 2) in dic:
            return find_summ(n + 2, summ + dic[n][0])
        else:
            return summ

    file1 = open('test')
    n = int(file1.readline())
    nums = []
    dic = {}
    minn_id = float('inf')

    for i in range(n):
        temp_arr = [int(i) for i in file1.readline().split()]
        nums.append(temp_arr)
        #dic[temp_arr[0]] = [0, 0]
        dic[temp_arr[0]] = []
        minn_id = min(minn_id, temp_arr[0])

    for i in range(n):
        dic[nums[i][0]] = []
        for j in range(1, len(nums[i])):
            if (nums[i][0] + j) in dic:
                #dic[nums[i][0]][j - 1] = nums[i][j]
                dic[nums[i][0]].append(nums[i][j])

    maxx_id = find_road(minn_id)
    minn_summ = find_summ(minn_id, 0)
    return (minn_summ, maxx_id)

def f2():
    f = open('test')
    n = int(f.readline())
    r = {}
    for x in f:
        a, b, c = map(int, x.split())
        r[a] = (b, c)
    s = 0
    a = min(r)
    while 1:
        if a + 1 in r and a + 2 in r:
            if r[a][0] < r[a][1]:
                s += r[a][0]
                a += 1
            else:
                s += r[a][1]
                a += 2
        elif a + 1 in r:
            s += r[a][0]
            a += 1
        elif a + 2 in r:
            s += r[a][1]
            a += 2
        else:
            return (s, a)

while True:
    ff = open('test', 'w')

    d = {}
    ff.write('1000\n')
    for i in range(1000):
        a = randint(1, 500)
        b = randint(1, 1000)
        c = randint(1, 1000)
        #print(a, b, c)
        ff.write(f'{a} {b} {c}\n')
    ff.close()

    res1 = f1()
    res2 = f2()
    #print(res1 == res2, res1, res2)
    if res1 != res2:
        print(res1)
        print(res2)

    f1()
    f2()