def to_base(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = str(temp_n % base) + temp_st
        temp_n //= base
    return temp_st
maxx = float('-inf')


for i in range(1, 1_000_000):
    n = to_base(i, 5)
    if n[-1] in '024':
        n += '2'
    else:
        n = '2' + n + '3'
    if int(n, 5) < 1000:
        maxx = max(maxx, i)
print(maxx)