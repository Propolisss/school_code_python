file = open('9.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    nums.sort()
    rep = []
    no_rep = []
    for j in nums:
        if nums.count(j) >= 2:
            rep.append(j)
        else:
            no_rep.append(j)
    if len(rep) == 0:
        if nums[2] ** 2 < (nums[-1] * nums[0]):
            count += 1
print(count)