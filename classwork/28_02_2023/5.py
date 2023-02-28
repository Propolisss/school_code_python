count = 0

for i in range(1, 1000 + 1):
    n = bin(i)[2:]

    for _ in range(2):
        if n.count('1') % 2 == 0:
            ind = n.find('1')
            n = n[:ind] + n[ind + 1:]
        else:
            n = (n.count('1') + 1) * '1'
    if int(n, 2) == 7:
        count += 1
print(count)