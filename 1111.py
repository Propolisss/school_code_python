file = open('26 (1).txt')
n = int(file.readline())
nums = sorted(set(int(i) for i in file))
maxx = float('-inf')
ans = set()

for i in range(len(nums)):
    curr = nums[i]
    count = 1
    for j in range(i + 1, len(nums)):
        if abs(curr - nums[j]) >= 56:
            curr = nums[j]
            count += 1
    maxx = max(maxx, count)
    if count == 177:
        ans.add(nums[i])
print(maxx, max(ans))