nums = [int(i) for i in input().split()]

if len(nums) == 0:
    print(nums)

for i in range(len(nums) - 1, -1, -1):
    if nums[i] + 1 < 10:
        nums[i] += 1
        print(nums)
        break
    else:
        nums[i] = 0
if nums[0] == 0:
    nums = [1] + nums
    print(nums)
    break