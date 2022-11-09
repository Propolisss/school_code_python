def to_six(n):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % 6}{temp_st}'
        temp_n //= 6
    return temp_st

nums = []
for i in range(1000000):
    st = to_six(i)
    if len(st) == 5:
        nums.append(st)

ch = '024'
nech = '135'
s = set()

for i in range(len(nums)):
    flag = 1
    for j in range(1, len(nums[i])):
        if ((nums[i][j - 1] in '024') and (nums[i][j] in '024')) or ((nums[i][j - 1] in '135') and (nums[j][j] in '135')):
            flag = 0
    if flag:
        s.add(nums[i])
print(len(s))