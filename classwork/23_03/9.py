list = []

for a in range(200):
    flag = 1
    for x in range(200):
        for y in range(200):
            flag *= ((3 * x + 4 * y) != 70) or (a > x) or (a > y)
            if not flag:
                break
    if flag:
        list.append(a)
print(min(list))