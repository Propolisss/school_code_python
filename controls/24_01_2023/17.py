nums = [int(i) for i in open('17 (2).txt')]
maxx = max(nums)

ans = []
nn = []

for i in range(2, len(nums)):
    if (nums[i - 2] + nums[i - 1] + nums[i]) <= maxx:
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
        nn.append(max(nums[i - 2], nums[i - 1], nums[i]))
        nn.append(min(nums[i - 2], nums[i - 1], nums[i]))
print(len(ans), max(nn) + min(nn))