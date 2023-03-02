for i in range(1, 1_000_000):
    n = bin(i)[2:]
    n += n[-1]
    n += '0' if n.count('1') % 2 == 0 else '1'
    n += '0' if n.count('1') % 2 == 0 else '1'
    if int(n, 2) > 90:
        print(i)
        break