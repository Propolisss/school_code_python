def change(n):
    return n.replace('1', '2').replace('0', '1').replace('2', '0')


ans = set()
for i in range(64, 1_000_000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = n[:-4] + change(n[-4:])
    else:
        n = n[:-5] + change(n[-5:-1]) + n[-1]
    if int(n, 2) == 64:
        print(i)
        break