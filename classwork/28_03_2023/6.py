from math import ceil

file = open('26_4408.txt')
n, t = map(int, file.readline().split())
nums = []

for i in file:
    nums.append([int(j) for j in i.split()][::-1])
mid = 0

for i in nums:
    mid += i[1]
mid = ceil(mid / len(nums))
super = []
common = []

for i in nums:
    if i[1] >= mid:
        super.append(i)
    else:
        common.append(i)
common.sort()
super.sort()
maxx_time = max(len(super), len(common))
my_time = 0
super_time = 0
count = 0

for i in range(maxx_time):
    if len(super) > 0:
        if my_time + super[0][0] + common[0][0] <= t:
            my_time += super[0][0]
            super_time += super[0][0]
            count += 1
            super.pop(0)
    if len(common) > 0:
        if my_time + super[0][0] <= t:
            my_time += common[0][0]
            common.pop(0)
            count += 1
        else:
            break
    else:
        break
print(count, super_time)