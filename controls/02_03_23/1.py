count = 0

for i in range(1, 1_000_000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n += bin(sum(int(i) for i in n))[2:]
    else:
        n = '1' + n + '00'
    if 500 <= int(n, 2) <= 700:
        count += 1
print(count)