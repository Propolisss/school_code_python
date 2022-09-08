



for i in range(10000):
    N = i
    n = bin(N)
    n = n[2:]
    if N % 2 != 0:
        n += '0'
    else:
        n = '1' + str(n)
    if n.count('1') % 2 == 0:
        n += '1'
    else:
        n += '0'
    if int(n, 2) > 228:
        print(i)
        break