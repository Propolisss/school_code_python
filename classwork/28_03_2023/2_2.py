file = open('26_5497.txt')
nums = []

for i in file:
    nums.append([int(j) for j in i.replace('A', '0').replace('B', '1').split()])
nums.sort()
flags = [0] * len(nums)
maxx = float('-inf')
count = 0

for i in range(len(nums)):
    if not(flags[i]):
        cur_count = 1
        flags[i] = 1
        last = nums[i]
        for j in range(i + 1, len(nums)):
            if not(flags[j]) and nums[j][1] != last[1] and abs(last[0] - nums[j][0]) >= 7:
                cur_count += 1
                flags[j] = 1
                last = nums[j]
        count += 1
        maxx = max(maxx, cur_count)
print(maxx, count)