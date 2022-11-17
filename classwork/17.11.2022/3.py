def f(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

summ = 0
for i in range(2, 10 + 1):
    if sum([int(j) for j in f(559, i)]) & 1:
        summ += i
print(summ)