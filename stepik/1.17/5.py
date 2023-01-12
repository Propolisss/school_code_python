nums = [int(i) for i in open('uX1sS0qUa.txt')]

summ = sum(int(str(abs(s))[0]) for s in nums)
ans = []

for i in range(1, len(nums)):
    if nums[i - 1] * nums[i] > summ:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))