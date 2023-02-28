for i in range(131, 255 + 1):
    n = '0' * (8 - len(bin(i)[2:])) + bin(i)[2:]
    n = n[:2] + n[6:]
    if int(n, 2) == 10:
        print(i)
        break