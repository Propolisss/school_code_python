file = open('27-47b.txt')
n = int(file.readline())
ost = []
summ = 0
maxx_summ = 0

for i in file:
    nums = [int(j) for j in i.split()]
    ost.append(abs(nums[0] - nums[1]))
    summ += min(nums)
    maxx_summ += max(nums)

lett = str(maxx_summ)[-1]
ost.sort()
old_summ = summ

for i in range(len(ost)):
    if str(summ + ost[i])[-1] == lett:
        summ += ost[i]
        break

curr_summ = 0
for i in range(len(ost)):
    curr_summ = ost[i]
    if str(old_summ + curr_summ)[-1] == lett and (old_summ + curr_summ) < summ:
        summ = old_summ + curr_summ
    else:
        continue
    for j in range(i + 1, len(ost)):
        if str(old_summ + curr_summ)[-1] == lett and (old_summ + curr_summ) < summ:
            summ = old_summ + curr_summ
        else:
            break
print(summ)