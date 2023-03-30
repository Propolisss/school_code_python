file = open('vJTtZeztY.txt')
nums = []

for i in file:
    nums.append([int(j) for j in i.replace('A', '0').replace('B', '1').split()])
nums.sort()

flags = [0] * len(nums)
maxx = float('-inf')
count = 0

for i in range(len(nums)):
    if not(flags[i]):
        inner_count = 1
        last = nums[i]
        flags[i] = 1
        for j in range(i + 1, len(nums)):
            if not(flags[j]):
                if abs(nums[j][0] - last[0]) >= 7 and nums[j][1] != last[1]:
                    inner_count += 1
                    flags[j] = 1
                    last = nums[j]
        count += 1
    maxx = max(maxx, inner_count)
print(maxx, count)