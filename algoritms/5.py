count = 0

for i in range(10, 10000):
    N = i
    n = bin(N)
    n = n[2:]
    n += n[-2]
    n += n[1]
    if 150 < int(n, 2) < 250:
        count += 1
print(count)