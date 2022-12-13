ans = []

for a in range(1_000):
    flag = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            flag += (((2 * x) + (3 * y)) == 101) and ((x + y) < a)
            if flag:
                break
        if flag:
            break
    if not flag:
        ans.append(a)

print(max(ans))