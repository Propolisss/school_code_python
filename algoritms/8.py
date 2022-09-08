count = 0


for i in range(1, 10000):
    N = i
    if N % 3 == 0:
        N //= 3
    else:
        N -= 1
    if N % 5 == 0:
        N //= 5
    else:
        N -= 1
    if N % 11 == 0:
        N //= 11
    else:
        N -= 1
    if N == 8:
        count += 1
print(count)