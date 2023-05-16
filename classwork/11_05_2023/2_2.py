from random import randint

#file = open('27_A_7275.txt')
#n, m = map(int, file.readline().split())

def f1():
    f = open('test')
    n, m = map(int, f.readline().split())
    summ = 0
    left = 0
    right = 0
    pref = [0] * n
    nums = [0] * n
    maxx = float('-inf')

    for i in range(n):
        n1, n2 = map(int, f.readline().split())
        n2 = (n2 + 29) // 30
        pref[i] = n2
        nums[i] = n1

    for i in range(n):
        while right < n and (nums[right] - nums[i]) <= m:
            summ += pref[right]
            right += 1
        while nums[i] - nums[left] > m:
            summ -= pref[left]
            left += 1
        maxx = max(maxx, summ)
    return(maxx)

def f2():
    fff = open('test')
    maxx = float('-inf')
    n, m = map(int, fff.readline().split())
    nums = [0] * n
    pref = [0] * n

    for i in range(n):
        n1, n2 = map(int, fff.readline().split())
        n2 = (n2 + 29) // 30
        pref[i] = n2
        nums[i] = n1

    for i in range(n):
        summ = 0
        for j in range(i, n):
            if (nums[j] - nums[i]) <= m:
                summ += pref[j]
            else:
                break
        for j in range(i - 1, -1, -1):
            if (nums[i] - nums[j]) <= m:
                summ += pref[j]
            else:
                break
        maxx = max(maxx, summ)
    return maxx




while True:
    s = set()
    ff = open('test', 'w')
    last = 0
    for i in range(1001):
        if i == 0:
            ff.write(f'{1000} {randint(1, 1000)}\n')
        else:
            nn = randint(1, 1000)
            s.add(last + nn)
            ff.write(f'{last + nn} {randint(1, 1000)}\n')
            last += nn
    ff.close()

    if f1() != f2():
        print(f1(), f2(), 'false')