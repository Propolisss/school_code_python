def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(2, 1_000):
    n1 = x * 15 ** 0 + 5 * 15 ** 1 + 1 * 15 ** 2 + x * 15 ** 3 + 3 * 15 ** 4
    n2 = 3 * int(f'3{x}51') ** 0 + 2 * int(f'3{x}51') ** 1 + 1 * int(f'3{x}51') ** 2
    n3 = x ** x
    n4 = 3 * int(f'1{x}3') ** 0 + x * int(f'1{x}3') ** 1 + 1 * int(f'1{x}3') ** 2
    n5 = 2 * (x + 1) ** 0 + x * (x + 1) ** 1 + 1 * (x + 1) ** 2
    summ = n1 + n2 + n3 + n4 + n5
    if summ % 13 == 0:
        print(to_base(summ, 13))
        break