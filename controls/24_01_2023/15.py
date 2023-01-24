ans = []


for a in range(0, 2_000):
    flag = 1
    for x in range(300):
        for y in range(300):
            flag *= ((y + 2 * x) != 48) or (a < x) or (a < y)
            if not flag:
                break
    if flag:
        ans.append(a)
print(max(ans))