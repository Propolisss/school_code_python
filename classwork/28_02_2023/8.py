ans = set()

for i in range(2, 1_000_000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += '0' if n.count('1') > n.count('0') else '1'
    if int(n, 2) > 80:
        ans.add(int(n, 2))
        print(min(ans))