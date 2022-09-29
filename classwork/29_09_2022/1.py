from itertools import *

s = list(map(''.join, product('АИКЛМЬ', repeat=6)))
ans = []
anss = []
nums = []
numss = []
count = 0

for i in range(len(s)):
    flag = 1
    count += 1
    for j in range(len(s[i])):
        if s[i].count(s[i][j]) != 1:
            flag *= 0
    if flag:
        if s[i][0] == 'К' and s[i][-1] == 'Ь':
            ans.append(s[i])
            nums.append(count)

count = 0
for i in range(len(s)):
    count += 1
    for j in range(len(nums)):
        if s[i] == ans[j][::-1]:
            anss.append(s[i])
            numss.append(count)

for i in range(len(nums)):
    for j in range(len(nums)):
        if numss[i] - nums[j] == 26655 and ans[i] == anss[j][::-1]:
            print(nums[j], numss[j])