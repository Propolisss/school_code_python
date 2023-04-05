file = open('17_7089.txt')
nums = [int(i) for i in file]
ans = []
minn = min(nums)

for i in range(1, len(nums)):
    if nums[i - 1] % 111 == minn or nums[i] % 111 == minn:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), min(ans))