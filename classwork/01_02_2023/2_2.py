from math import *

file = open('27_A.txt')
nums = [i.split() for i in file]
minn = float('inf')

for i in range(len(nums)):
    summ = 0
    for j in range(len(nums)):
        if i == j:
            continue
        summ += abs((int(nums[j][0]) - int(nums[i][0]))) * (ceil(int(nums[j][1]) / 36))
    minn = min(minn, summ)
print(minn)