

for i in range(1, 10000):
    n = bin(i)[2:]
    if (n.count('1') > n.count('0')):
        n += '1'
    else:
        n += '0'
    if (int(n, 2) < 100):
        print(int(n, 2))
