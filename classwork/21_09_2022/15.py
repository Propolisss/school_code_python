p = []
q = []

for i in range(1, 41):
    p.append(i)
for i in range(25, 121):
    q.append(i)

for i in range(-100, 100):
    flag = True
    for j in range(-100, 100):
        for x in range(100):
            flag *= (x in q) >= ((not(x in p) and (x in q)) <= (i <= x <= j))
        if flag:
            print(i, j)