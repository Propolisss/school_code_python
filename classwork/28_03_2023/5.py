file = open('26_281.txt')
n = int(file.readline())
nums = sorted([int(i) for i in file])
perc = n // 20
summ_perc = 0

for i in range(500):
    summ_perc += nums[i] + nums[-i - 1]
print(sum(nums) - summ_perc, nums[-501])