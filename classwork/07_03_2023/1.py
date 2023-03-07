file = open('26_1379.txt')
s, n = map(int, file.readline().split())
nums = [int(i) for i in file]
nums.sort()
flags = [0] * n
minn = float('inf')
maxx = float('-inf')


summ = 0
count = 0
for j in range(n):
    if not(flags[j]):
        if summ + nums[j] <= s:
            summ += nums[j]
            flags[j] = 1
            count += 1
        maxx = max(maxx, count)
new_nums = nums[flags.index(0):]
# if len(new_nums) & 1:
#     new_maxx = new_nums[-1]
#     del new_nums[-1]
#
# maxx2 = float('-inf')
#
# for i in range(len(new_nums) // 2):
#     maxx2 = max(maxx2, new_nums[-i - 1] + new_nums[i])
# print(maxx, max(maxx2, new_maxx))
ans = set()

for i in range(len(new_nums)):
    for j in range(i + 1, len(new_nums)):
        if new_nums[i] + new_nums[j] >= new_nums[-1]:
            ans.add(new_nums[i] + new_nums[j])
print(maxx, sorted(ans))