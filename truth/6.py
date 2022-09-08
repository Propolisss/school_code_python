list = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))