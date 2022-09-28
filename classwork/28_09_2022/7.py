n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))
del nums[::2]

print(nums)