minn = float('inf')

for i in range(1, 10_000_000):
    n = bin(i)[2:]
    n += str(sum(int(i) for i in n) % 2)
    n += str(sum(int(i) for i in n) % 2)
    if int(n, 2) > 396:
        minn = min(minn, int(n, 2))
print(minn)