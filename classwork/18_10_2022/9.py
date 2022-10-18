def to_nine(n):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % 9}{temp_st}'
        temp_n //= 9
    return temp_st

count = 0
n1 = int('1000000', 9)
n2 = int('8888888', 9)
print(n1, n2)

for i in range(n1, n2 + 100):
    if i % 100000 == 0:
        print(i)
    st = to_nine(i)
    if len(st) == 7:
        if (st[-1] not in '347'):
            flag = 1
            for j in range(2, len(st)):
                if (st[j - 2] == st[j - 1] and st[j - 1] == st[j]):
                    flag = 0
            if flag:
                count += 1
print(count)