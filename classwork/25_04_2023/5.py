ans = set()

for i in range(1, 10):
    n = bin(i)[2:]
    n = n.replace('1', '11').replace('0', '00')
    if int(n, 2) > 63:
        ans.add(int(n, 2))
print(min(ans))