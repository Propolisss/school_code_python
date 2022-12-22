def quick_merge(nums_):
    merged = []
    all_len = 0
    for i in nums_:
        all_len += len(i)

    flag = [[] for i in range(len(nums_))]
    for i in range(len(nums_)):
        flag[i].extend([0] * len(nums_[i]))

    curr_num = float('inf')
    curr_ind = []
    all_ind = []


    for i in range(all_len):
        j = 0
        curr_num = float('inf')
        for k in range(len(nums_)):
            j = 0
            while j < len(nums_[k]) and flag[k][j] != 0:
                j += 1
            if j >= len(nums_[k]):
                continue
            all_ind.append([k, j])
        for k in range(len(all_ind)):
            if nums_[all_ind[k][0]][all_ind[k][1]] <= curr_num:
                curr_num = nums_[all_ind[k][0]][all_ind[k][1]]
                curr_ind = [all_ind[k][0], all_ind[k][1]]
        flag[curr_ind[0]][curr_ind[1]] = 1
        merged.append(curr_num)
        all_ind.clear()
        curr_ind.clear()
    return merged



nums = [[] for i in range(int(input()))]

for i in range(len(nums)):
    nums[i] = [int(i) for i in input().split()]

print(*quick_merge(nums))