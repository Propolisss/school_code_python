count = 0

for i in range(100, 200 + 1):
    n = bin(i)[2:]
    if len(n) % 2 == 0:
        n += '10'
    else:
        n = '11' + n
    if int(n, 2) % 2 == 0:
        count += 1
print(count)