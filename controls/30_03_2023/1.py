file = open('bc2SR4ATb.txt')

n = int(file.readline())
nums = [int(i) for i in file]
nums.sort(reverse=True)
perc = int(n * (1 / 4))
summ_check = int((sum(nums[-perc:]) / 2) + sum(nums[:-perc]))

summ = 0
inner_count = 0

for i in range(len(nums)):

    if inner_count == 3:
        summ += nums[i] // 2
        inner_count = 0
    else:
        summ += nums[i]
        inner_count += 1
print(summ, summ_check)