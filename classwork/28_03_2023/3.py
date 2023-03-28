file = open('26_1868.txt')
n = int(file.readline())
rows = dict()
maxx_row = float('-inf')
dic = dict()

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in rows:
        rows[nums[0]].append(nums[1])
    else:
        rows[nums[0]] = [nums[1]]
    maxx_row = max(maxx_row, nums[0])

maxx = float('-inf')
for i in range(maxx_row - 1, -1, -1):
    if i in rows and len(rows[i]) >= 2:
        rows[i].sort()
        for j in range(1, max(rows[i])):
            if (j - 1) in rows[i] and (j + 2) in rows[i]:
                print(i, j)
                break
