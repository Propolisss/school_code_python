for i in range(10000):
    s = i
    n = 200
    while s > 0:
        s = s // 4
        n = n - 6
    if n == 170:
        print(i)
