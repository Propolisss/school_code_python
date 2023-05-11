nums = [int(i) for i in open('17_2997.txt')]
lets = dict()

for i in nums:
    if len(str(abs(i))) == 3:
        if str(abs(i))[1] in lets:
            lets[str(abs(i))[1]] += 1
        else:
            lets[str(abs(i))[1]] = 1
maxx = max(lets.values())
maxx_let = ''

for i in lets:
    if lets[i] == maxx:
        maxx_let = i
ans = []

for i in range(1, len(nums)):
    if str(nums[i - 1])[-1] == maxx_let or str(nums[i])[-1] == maxx_let:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))