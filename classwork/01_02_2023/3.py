file = open('26.txt')
n = int(file.readline())
nums = sorted(set([int(i) for i in file]))
maxx = float('-inf')
minn = float('inf')
ans = set()

for i in range(len(nums)):
    count = 1
    current = nums[i]
    for j in range(len(nums)):
        if i == j:
            continue
        if (nums[j] - current) >= 3:
            count += 1
            current = nums[j]
    if count > maxx:
        ans.add(nums[i])
        maxx = count
        minn = nums[i]
    elif count == maxx:
        ans.add(nums[i])
        maxx = count
        minn = min(minn, nums[i])
print(maxx, maxx(ans))