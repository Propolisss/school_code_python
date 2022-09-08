count = 0

for i in range(10000):
    x = i
    s = 6 * (x // 5)
    n = 1
    while s < 300:
        s = s + 35
        n = n * 2
    if n == 64:
        count += 1
print(count)