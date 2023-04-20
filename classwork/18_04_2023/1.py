file = open('27-B_2133.txt')
n = int(file.readline())
from random import randint
def f2(num):
    # k = [float('inf') for _ in range(37)]
    # lens = [0] * 37
    # pref = [0] * (len(num) + 2)
    # summ = 0
    # maxx = float('-inf')
    # minn_len = float('inf')
    #
    # for i in range(len(num)):
    #     x = num[i]
    #     if i == 0:
    #         first = x
    #     summ += x
    #     pref[i + 1] = summ
    #     if i == 0:
    #         if summ < k[summ % 37] or (summ == k[summ % 37] and (i + 1) < lens[summ % 37]):
    #             k[summ % 37] = summ
    #             lens[summ % 37] = i + 1
    #         continue
    #
    #     if summ % 37 == 0 and summ > maxx and (first + x) % 73 == 0:
    #         maxx = summ
    #         minn_len = i + 1
    #     elif summ % 37 == 0 and summ == maxx and (first + x) % 73 == 0:
    #         if (i + 1) < minn_len:
    #             minn_len = i + 1
    #
    #     s1 = (summ - k[summ % 37]) if k[summ % 37] != float('inf') else 0
    #     l1 = (i + 1) - lens[summ % 37]
    #
    #
    #
    #     first = pref[i + 2 - l1] - pref[i + 2 - l1 - 1]
    #     last = x
    #
    #     # if s1 > 0:
    #     #     if (first + last) % 73 == 0:
    #     #         print(i, l1, s1)
    #
    #     if s1 > maxx and (first + last) % 73 == 0:
    #         maxx = s1
    #         minn_len = l1
    #     elif s1 == maxx and l1 < minn_len and s1 > 0 and (first + last) % 73 == 0:
    #         minn_len = l1
    #
    #     if summ < k[summ % 37] or (summ == k[summ % 37] and (i + 1) < lens[summ % 37]):
    #         k[summ % 37] = summ
    #         lens[summ % 37] = i + 1
    # return (maxx, minn_len)
    summ = 0
    maxx = float('-inf')
    minn_len = 0
    k = [[[float('inf'), 0]] * 73 for i in range(37)]

    for i in range(len(num)):
        summ += num[i]
        x = num[i]

        if summ % 37 == 0 and (x + num[0]) % 73 == 0:
            maxx = summ
            minn_len = i + 1

        if k[summ % 37][(73 - x % 73) % 73][0] != float('inf'):
            if (summ - k[summ % 37][(73 - x % 73) % 73][0] > maxx) or (summ - k[summ % 37][(73 - x % 73) % 73][0] == maxx and i + 1 - k[summ % 37][(73 - x % 73) % 73][1] < minn_len):
                maxx = summ - k[summ % 37][(73 - x % 73) % 73][0]
                minn_len = i + 1 - k[summ % 37][(73 - x % 73) % 73][1]

        if k[(summ - x) % 37][x % 73][0] == float('inf'):
            k[(summ - x) % 37][x % 73] = [summ - x, i]
    return (maxx, minn_len)
def f1(num):
    maxx = float('-inf')
    minn_lenn = float('inf')
    fs = float('-inf')
    ls = float('-inf')
    for i in range(len(num)):
        summ = 0
        nums = []
        for j in range(i, len(num)):
            nums.append(num[j])
            summ += num[j]
            if len(nums) >= 2 and (nums[0] + nums[-1]) % 73 == 0 and summ % 37 == 0:
                if summ > maxx or (summ == maxx and (j - i + 1) < minn_lenn):
                    maxx = summ
                    minn_lenn = j - i + 1
                    fs = num[i]
                    ls = num[j]
    return (maxx, minn_lenn, fs, ls)

nums = [int(i) for i in file]
print(f2(nums))

while True:
    nums = [randint(1, 10000) for i in range(1000)]
    res1 = f1(nums)
    res2 = f2(nums)
    print(res1, res2, res1[:2] == res2)