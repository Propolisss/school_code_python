nums = [int(i) for i in open('17 (1).txt')]
ans = []

for i in range(len(nums)):
    if ((nums[i] % 10 == 5) or (nums[i] % 10 == 7)) and (nums[i] % 9 != 0) and (nums[i] % 11 != 0):
        ans.append(nums[i])
ans.sort()
print(len(ans), ans[0] + ans[-1])