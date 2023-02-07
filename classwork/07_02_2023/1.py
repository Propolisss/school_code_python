file = open('27-24b.txt')
n = int(file.readline())
ost = []
summ = 0

for i in file:
    nums = [int(j) for j in i.split()]
    summ += min(nums)
    ost.append(abs(nums[0] - nums[1]))
ost.sort()
old_summ = summ

for i in range(len(ost)):
    if str(summ + ost[i])[-1] != '6':
        summ += ost[i]
        break

curr_summ = 0
for i in range(len(ost)):
    curr_summ = ost[i]
    if str(old_summ + curr_summ)[-1] != '6' and (old_summ + curr_summ) < summ:
        summ = (old_summ + curr_summ)
    else:
        continue
    for j in range(i, len(ost)):
        curr_summ += ost[i]
        if str(old_summ + curr_summ)[-1] != '6' and (old_summ + curr_summ) < summ:
            summ = (old_summ + curr_summ)
        else:
            break
print(summ)