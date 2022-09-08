




for i in range(10000):
    N = i
    n = bin(N)
    n = n[2:]
    if n.count('1') % 2 != 0:
        n += '11'
    else:
        n = '11' + str(n)
    if int(n, 2) > 102:
        print(i)
        break