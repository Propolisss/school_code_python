nums = [int(i) for i in open('17_6024.txt')]
maxx = float('-inf')
ans = []

for i in nums:
    if str(i)[-2:] == '12':
        maxx = max(maxx, i)

for i in range(1, len(nums)):
    if (str(nums[i - 1])[-2:] == '12') ^ (str(nums[i])[-2:] == '12'):
        if (nums[i - 1] + nums[i]) ** 2 < maxx ** 2:
            ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))