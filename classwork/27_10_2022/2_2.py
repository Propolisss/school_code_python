nums = [int(i) for i in input().split()]

nums[nums.index(max(nums))], nums[nums.index(min(nums))] = min(nums), max(nums)
print(*nums)