nums = []

def to_nine(n):
    temp_st = ''
    temp_n = n
    while temp_n != 0:
        temp_st += str(temp_n % 9)
        temp_n //= 9
    return temp_st[::-1]


for i in range(1000000):
    nums.append(to_nine(i))

count = 0
for i in range(1, len(nums)):
    if (int(nums[i][0]) % 2 == 0) and (nums[i][-1] != '1' and nums[i][-1] != '8') and (nums[i].count('3') <= 1) and (len(nums[i]) == 5):
        count += 1
print(count)