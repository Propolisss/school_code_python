list = []

for a in range(1000):
    flag = 1
    for x in range(1000):
        for y in range(1000):
            flag *= (x + 2 * y < a) or (y > x) or (x > 30)
            if not flag:
                break
    if flag:
        list.append(a)
print(min(list))