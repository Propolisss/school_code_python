


for i in range(10000):
    N = i
    last = N % 10
    n = str(N) + str(last)
    n = bin(int(n))
    n = n[2:]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if int(n, 2) > 413:
        print(i)
        break