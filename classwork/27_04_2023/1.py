file = open('26_7626.txt')
k = int(file.readline())
n = int(file.readline())
nums = sorted([list(map(int, i.split())) for i in file])
bags = [[] for _ in range(k)]
count = 0
last = [0] * 10
dic = [[] for _ in range(1440)]

for i in range(n):
    if any(len(j) == 0 for j in bags):
        for j in range(k):
            if len(bags[j]) == 0:
                bags[j] = [nums[i][1]]
                dic[nums[i][0]].append(j + 1)
                last.append(nums[i][0])
                last.pop(0)
                count += 1
                break
    elif any(j[0] < nums[i][0] for j in bags):
        for j in range(k):
            if bags[j][0] < nums[i][0]:
                bags[j] = [nums[i][1]]
                dic[nums[i][0]].append(j + 1)
                last.append(nums[i][0])
                last.pop(0)
                count += 1
                break
print(count, last, dic[last[-1]])