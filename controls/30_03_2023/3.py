file = open('v5k88VKyR.txt')
n = int(file.readline())
nums = sorted(set([int(i) for i in file]))
ans = set()
maxx = float('-inf')

for i in range(len(nums)):
    count = 1
    last = nums[i]

    for j in range(i + 1, len(nums)):
        if abs(nums[j] - last) >= 11:
            count += 1
            last = nums[j]
    maxx = max(maxx, count)
    if count == 854:
        ans.add(nums[i])
print(maxx, ans)