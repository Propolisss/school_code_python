n_nums = []
nums = []
file = open('dificult/26-53.txt')
count = 0
maxx = 0

for i in file:
    if int(i) & 1:
        n_nums.append(int(i))
    nums.append(int(i))
nums.pop(0)

for j in range(len(n_nums)):
    for k in range(j + 1, len(n_nums)):
        if ((n_nums[j] + n_nums[k]) // 2) in nums:
            count += 1
            if (n_nums[j] + n_nums[k]) // 2 > maxx:
                maxx = (n_nums[j] + n_nums[k]) // 2

print(count, maxx)
print(n_nums)
print(nums)