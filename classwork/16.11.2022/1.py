nums = [int(i) for i in open('17-328.txt')]

max50 = float('-inf')

for i in nums:
    if i % 50 == 0:
        max50 = max(max50, i)

ans = []

for i in range(2, len(nums)):
    n1 = nums[i - 2]
    n2 = nums[i - 1]
    n3 = nums[i]
    summs = [n1 + n2, n2 + n3, n1 + n3]
    if all(str(j) == str(j)[::-1] for j in summs) and max(summs) < max50:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))