nums = []

for a in range(0, 1000):
    flag = 1
    for x in range(0, 2000):
        flag *= (x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0))
        if not flag:
            break
    if flag:
        nums.append(a)
print(min(nums))