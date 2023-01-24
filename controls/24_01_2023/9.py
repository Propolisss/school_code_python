file = open('9.txt')
nums = []

for i in file:
    nums.append([int(i) for i in i.split()])


count = 0

for i in range(len(nums)):
    j = 0
    flag1 = 0
    flag2 = 0

    while j < len(nums[i]) - 1 and (nums[i][j] > nums[i][j + 1]):
        j += 1
        flag1 = True

    while j < len(nums[i]) - 1 and (nums[i][j] < nums[i][j + 1]):
        j += 1
        flag2 = True

    if (j == (len(nums[i]) - 1)) and flag1 and flag2:
        count += 1
print(count)