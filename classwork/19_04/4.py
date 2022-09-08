for i in range(1, 1000):
    N = i
    n = bin(N)
    nn = n[2:]
    if N & 1:
        nn += '11'
    else:
        nn += '10'
    if nn.count('1') % 2 == 0:
        nn += '0'
    else:
        nn += '1'
    if int(nn, 2) > 53:
        print(i)
        break