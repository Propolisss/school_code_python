def to_n(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

for i in range(2, 100):
    if (to_n(41, i)[-1] == '2') and (to_n(131, i)[-1] == '1'):
        print(i)