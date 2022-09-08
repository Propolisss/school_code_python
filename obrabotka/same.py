n = int(input())
nn = 0
flag = 0
temp = 0

while n != 0:
    if nn == temp:
        flag = 1
    else:
        flag = 0
        break
    nn = n % 10
    n //= 10
    temp = n % 10
if flag:
    print('YES')
else:
    print('NO')