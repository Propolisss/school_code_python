nums = [int(i) for i in input().split()]
ans = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            ans.append(str(nums[i]) + str(nums[j]))
print(len(ans))