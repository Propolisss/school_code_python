nums = []

for a in range(-100, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            flag *= (2 * x + 3 * y != 101) or (x + y >= a)
    if flag:
        nums.append(a)
print(max(nums))