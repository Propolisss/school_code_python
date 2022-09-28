n = int(input())
nums = []
ans = []

for i in range(n):
    nums.append(int(input()))

for i in range(1, len(nums)):
    ans.append(nums[i - 1] + nums[i])
print(ans)