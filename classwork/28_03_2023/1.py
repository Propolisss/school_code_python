file = open('26_6031.txt')
n = int(file.readline())
nums = [int(i) for i in file]
nums.sort()
ans = set()
maxx = float('-inf')
dic = dict()

for i in range(len(nums)):
    count = 1
    last = nums[i]
    for j in range(i + 1, len(nums)):
        if abs(nums[j] - last) >= 6:
            count += 1
            last = nums[j]
    maxx = max(maxx, count)
    if count in dic:
        dic[count].add(nums[i])
    else:
        dic[count] = {nums[i]}
print(maxx, dic[maxx])