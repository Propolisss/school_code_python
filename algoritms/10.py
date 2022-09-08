



for i in range(1, 255 + 1):
    N = i
    n = bin(N)
    n = n[2:]
    if len(n) != 8:
        n += '0' * (8 - len(n))
    n = n[:2] + n [-2:] 
    if i > 130 and int(n, 2) == 10:
        print(i)
        break