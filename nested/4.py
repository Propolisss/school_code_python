n = int(input())

for i in range(1, n + 1):
    if i > n // 2 + 1:
        for j in range(n // 2, 0, -1):
            print('*' * j)
        break
    else:
        print('*' * i)