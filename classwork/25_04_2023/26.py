file = open('26_4115.txt')
n = int(file.readline())
dic = dict()
maxx_ind = float('-inf')

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in dic:
        if nums[1] not in dic[nums[0]]:
            dic[nums[0]].append(nums[1])
    else:
        dic[nums[0]] = [nums[1]]
    dic[nums[0]].sort()
    maxx_ind = max(maxx_ind, nums[0])

maxx = float('-inf')
ans = dict()

for i in range(maxx_ind - 1, -1, -1):
    if i in dic:
        curr = 1
        curr_maxx = float('-inf')
        for j in range(len(dic[i]) - 1):
            if dic[i][j + 1] - dic[i][j] == 1:
                curr += 1
            else:
                curr = 1
        print(dic[i], curr)
        curr_maxx = max(curr_maxx, curr)
        maxx = max(maxx, curr)
        if curr_maxx in ans:
            ans[curr_maxx].append(i)
        else:
            ans[curr_maxx] = [i]
print(maxx, *ans[maxx])