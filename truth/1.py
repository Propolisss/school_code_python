list = []

for a in range(1, 100):
    flag = 1
    for x in range(1, 100):
        for y in range(1, 100):
            flag *= (x < 9) <= ((5 * y < x) <= (2 * x * y < a))
            if not flag:
                break
    if flag:
        list.append(a)
print(min(list))