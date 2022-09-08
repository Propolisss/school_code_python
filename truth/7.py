p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}

list = {}

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= ((x in a) <= (x in p)) and (((x in q) <= (x not in a)))
        if not flag:
            break
    if flag:
        list.append(a)
print(list)