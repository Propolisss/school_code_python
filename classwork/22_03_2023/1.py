file = open('26-94.txt')

n, k = map(int, file.readline().split())
floor1 = dict()
floor2 = dict()

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] == 1:
        if nums[1] in floor1:
            floor1[nums[1]][nums[2] - 1] = 1
        else:
            floor1[nums[1]] = [0] * k
            floor1[nums[1]][nums[2] - 1] = 1
    else:
        if nums[1] in floor2:
            floor2[nums[1]][nums[2] - 1] = 1
        else:
            floor2[nums[1]] = [0] * k
            floor2[nums[1]][nums[2] - 1] = 1
maxx_all = max(max(floor1), max(floor2))
count = 0
maxx = float('-inf')

for i in range(maxx_all, -1, -1):
    if i in floor1:
        if floor1[i][:4] == [0, 0, 0, 0] or floor1[i][2:] == [0, 0, 0, 0]:
            count += 1
            maxx = max(maxx, i)
    if i in floor2:
        if floor2[i][:4] == [0, 0, 0, 0] or floor2[i][2:] == [0, 0, 0, 0]:
            count += 1
            maxx = max(maxx, i)
print(maxx, count)