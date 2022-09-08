list = []

for a in range(500):
    flag = 1
    for x in range(1, 500):
        for y in range(1, 500):
            flag *= ((y - 40 < a) and (30 - y < a)) or (x * y > 20)
            if not flag:
                break
    if flag:
        list.append(a)
print(min(list))