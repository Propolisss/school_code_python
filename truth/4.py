list = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= ((x % a == 0) and (x % 21 == 0)) <= (x % 18 == 0)
        if not flag:
            break
    if flag:
        list.append(a)
print(min(list))