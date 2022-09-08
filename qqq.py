list = []

for a in range(1, 1000):
    flag = 1
    for x in range(10000):
        for y in range(10000):
            flag *= ((680 * y + 256 * x) < a) or ((5 * x + 3 * y) > 11112)
            if not flag:
                break
    if flag:
        list.append(a)
print(list)