ans = set()


for i in range(100, 200 + 1):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[:-2] + '00'
    else:
        n = '11' + n[:-2] + '11'
    if int(n, 2) % 3 == 0:
        ans.add(int(n, 2))
print(sum(ans))