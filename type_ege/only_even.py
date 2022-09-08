#count = 0

#for i in range(10):
#    n = int(input())
#    if n % 2 == 0:
#        count += 1
#if count == 10:
#    print('YES')
#else:
#    print('NO')


#flag = 1

#for i in range(10):
#    n = int(input())
#    if n % 2 == 0:
#        flag *= 1
#    else:
#        flag *= 0
#if flag:
#    print('YES')
#else:
#    print('NO')


flag = 1

for i in range(10):
    n = int(input())
    if n % 2 == 0:
        flag *= 1
    else:
        flag *= 0
        print('NO')
        break
if flag:
    print('YES')