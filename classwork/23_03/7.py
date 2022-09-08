list = []

for a in range(1, 10000):
    flag = 1
    for x in range(1, 10000):
        flag *= (x % a == 0) <= ((x % 21 == 0) + (x % 35 == 0))
        if not flag:
            break
    if flag:
        list.append(a)
        break
print(min(list))