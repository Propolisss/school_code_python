



for i in range(10000):
    N = i
    n = bin(N)
    n = n[2:]
    if N % 2 != 0:
        n = '10' + str(n)
        n += '11'
    else:
        n = '1' + str(n)
        n += '00'
    if int(n, 2) > 1023:
        print(int(n ,2))
        break