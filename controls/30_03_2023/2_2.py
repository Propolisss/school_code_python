file = open('26_7274.txt')
n = int(file.readline())
rows = dict()
maxx_row = float('-inf')

for i in file:
    nums = [int(j) for j in i.split()]

    if nums[0] in rows:
        rows[nums[0]].append(nums[1])
    else:
        rows[nums[0]] = [nums[1]]
    maxx_row = max(maxx_row, nums[0])

for i in range(maxx_row - 1, -1, -1):
    if i in rows and len(rows[i]) >= 2:
        rows[i].sort()
        for j in range(1, len(rows[i])):
            if abs(rows[i][j - 1] - rows[i][j]) == 14:
                print(i, rows[i][j - 1] + 1)
                break