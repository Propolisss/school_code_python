ans = set()

for i in range(1, 10_000_000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    if int(n, 2) == 50:
        print(i)
#print(min(ans))