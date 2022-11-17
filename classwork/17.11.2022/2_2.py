def f(n, base):
    temp_n = n
    temp_st = ''
    
    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

for x in range(1, 10_000_000):
    z = f(5 ** 2026 + 7 * 5 ** 1013 + 107 - x, 6)
    if z.count('5') - z.count('0') == 28:
        print(x)
        break
