file = open('27A_3378.txt')
n, k = map(int, file.readline().split())
minn = float('inf')
minn_ind = float('inf')
nums = [int(i) for i in file]

for i in range(len(nums)):
    print(i)
    summ = 0
    for j in range(len(nums)):
        r = abs(j - i)
        summ += nums[j] * ((min(r, n - r) * k) ** 2)
    if summ < minn:
        minn = summ
        minn_ind = i + 1
print(minn_ind, minn)