with open('17.txt') as file:
    nums = [int(i) for i in file]

minn = 10 ** 10

for i in range(len(nums)):
    if nums[i] % 43 == 0:
        minn = min(minn, nums[i])

ans = []
for i in range(1, len(nums)):
    if ((nums[i - 1] + nums[i]) % minn == 0) or (str(nums[i - 1])[-1] == '7' or str(nums[i])[-1] == '7'):
        ans.append(nums[i])
        ans.append(nums[i - 1])
print(len(ans) / 2, max(ans))