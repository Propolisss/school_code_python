list = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))