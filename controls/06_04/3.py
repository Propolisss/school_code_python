list = []

for a in range(1000):
    flag = 1
    for x in range(1000):
        flag *= (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))