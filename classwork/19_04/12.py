for i in range(1, 1000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L+1
        if M < (x % 8):
            M = x % 8
        x = x // 8
    print(L, M)