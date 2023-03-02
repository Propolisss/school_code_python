ans = set()

for n in range(1, 1000):
    for m in range(1, 1000):
        p1 = 1
        st = str(n) + str(m)
        for i in st:
            if i in '2468':
                p1 *= int(i)
        p2 = 1
        for i in st:
            if i in '13579':
                p2 *= int(i)
        if n == 120 and abs(p1 - p2) == 29:
            ans.add(m)
print(min(ans), ans)