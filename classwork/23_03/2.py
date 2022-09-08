list = []

for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        flag *= (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))
        if not flag:
            break
    if flag:
        list.append(a)
print(max(list))