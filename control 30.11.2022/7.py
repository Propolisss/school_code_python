nums = [int(i) for i in open('17-338.txt')]
minn = min(nums)
ans = []

for i in range(1, len(nums)):
    n1 = nums[i - 1]
    n2 = nums[i]
    if ((n1 % 117) == minn) or ((n2 % 117) == minn):
        ans.append(n1 + n2)
print(len(ans), max(ans))