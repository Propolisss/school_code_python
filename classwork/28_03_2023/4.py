from math import ceil

file = open('26_589.txt')
n = int(file.readline())
nums = sorted([int(i) for i in file])
summ = sum(nums)
curr_summ = 0
maxx_five = ceil(max(nums) / 500)
arr = [[] for _ in range(maxx_five + 1)]
maxx = float('-inf')

for i in nums:
    arr[ceil(i / 500)].append(i)

for i in range(maxx_five + 1):
    inner_summ = 0
    for j in range(len(arr[i]) // 2):
        curr_summ += arr[i][-j - 1] + (arr[i][j] / 2)
        maxx = max(maxx, arr[i][j] / 2)
    else:
        if len(arr[i]) != 0 and len(arr[i]) & 1:
            curr_summ += arr[i][len(arr[i]) // 2]
print(int(summ - curr_summ), int(maxx))