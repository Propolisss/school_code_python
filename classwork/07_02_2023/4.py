file = open('27-45a.txt')
n = int(file.readline())
ost = []
flags = [0] * n
summ1 = 0
summ2 = 0
summ3 = 0

for i in file:
    nums = [int(j) for j in i.split()]
    nums.sort()
    ost.append([nums[1] - nums[0], nums[2] - nums[0]])
    summ1 += nums[-1]
    summ2 += nums[-2]
    summ3 += nums[-3]
ost.sort()

if summ1 % 2 == 0:
    for i in range(len(ost)):
        if (summ1 - ost[i][0]) & 1 and not flags[i]:
            summ1 -= ost[i][0]
            summ3 += ost[i][0]
            flags[i] = 1
            break
        elif (summ1 - ost[i][1]) & 1 and not flags[i]:
            summ1 -= ost[i][1]
            summ3 += ost[i][1]
            flags[i] = 1
            break
if summ2 % 2 == 0:
    for i in range(len(ost)):
        if (summ2 - ost[i][0]) & 1 and not flags[i]:
            summ2 -= ost[i][0]
            summ3 += ost[i][0]
            flags[i] = 1
            break
        elif (summ2 - ost[i][1]) & 1 and not flags[i]:
            summ2 -= ost[i][1]
            summ3 += ost[i][1]
            flags[i] = 1
            break
print(summ3)