list = []

for a in range(10000):
    flag = 1
    for x in range(10000):
        flag *= ((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & a != 0))
        if not flag:
            break
    if flag:
        list.append(a)
        break
print(min(list))