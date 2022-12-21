def quick_merge(nums_):
    merged = []
    left = 0
    right = 0
    all_len = 0
    for i in nums_:
        all_len += len(i)

    flag = [[] for i in range(len(nums_))]
    for i in nums_:
        flag[i].extend([0] * len(nums_[i]))

    curr_num = float('-inf')
    curr_ind = []

    for i in range(all_len):
        j = 0
        for k in range(len(nums_)):
            while nums_[k][j] != 0 and j < len(nums_[k]):
                j += 1
            curr_ind.append([k, j])






nums = [[] for i in range(int(input()))]

for i in range(len(nums)):
    nums[i] = [int(i) for i in input().split()]

print(quick_merge(nums))