file = open('26-86.txt')
n = int(file.readline())
dishes = dict()
maxx = float('-inf')
for i in file:
    nums = [int(j) for j in i.split()]
    maxx = max(maxx, nums[0])
    if nums[-1] in dishes:
        dishes[nums[-1]].append(nums[0])
    else:
        dishes[nums[-1]] = [nums[0]]
count = 0
maxx_time = float('-inf')
maxx_ind = -1
all_time = [0] * maxx
for i in dishes:
    time = []
    dishes[i].sort()
    for j in range(0, len(dishes[i]), 2):
        if j == len(dishes[i]) - 1:
            continue
        else:
            time.append(abs(dishes[i][j] - dishes[i][j + 1]))
            if abs(dishes[i][j] - dishes[i][j + 1]) <= 60:
                for l in range(dishes[i][j], dishes[i][j + 1] + 1)
    for k in time:
        if k <= 60:
            count += 1
    if len(time) > 0:
        if (sum(time) / len(time)) > maxx_time:
            maxx_time = (sum(time) / len(time))
            maxx_ind = i
print(count, maxx_ind)