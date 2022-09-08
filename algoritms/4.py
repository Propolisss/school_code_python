



for i in range(10000):
    N = i
    R = bin(N)
    R = R[2:]
    if N % 2 == 0:
        R += '01'
    else:
        R += '10'
    if int(R, 2) > 73:
        print(i)
        break