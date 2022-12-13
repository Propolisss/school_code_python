

for i in range(2, 100):
    n = bin(i)[2:]
    c1 = n.count('1')
    c0 = n.count('0')
    if c1 == c0:
        n += n[-1]
    else:
        if c1 < c0:
            n += '1'
        else:
            n += '0'

    c1 = n.count('1')
    c0 = n.count('0')
    if c1 == c0:
        n += n[-1]
    else:
        if c1 < c0:
            n += '1'
        else:
            n += '0'

    c1 = n.count('1')
    c0 = n.count('0')
    if c1 == c0:
        n += n[-1]
    else:
        if c1 < c0:
            n += '1'
        else:
            n += '0'
    if i > 65:
        if int(n, 2) % 4 == 0:
            print(i, int(n, 2), int(n, 2) / 4)