a = int(input())

if ((a % 10) % 2 == 0) and (((a % 100) // 10) % 2 == 0):
    print('YES!')
else:
    print('NO')