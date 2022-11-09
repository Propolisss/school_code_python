nums = [int(i) for i in open('17 (1).txt')]

count_abs = 0
ans = []

for i in nums:
    if abs(i) < 100:
        count_abs += 1

for i in range(1, len(nums)):
    n1 = nums[i - 1]
    n2 = nums[i]
    sr = (n1 + n2) / 2
    if sr > count_abs:
        ans.append(n1 + n2)
print(len(ans), max(ans))