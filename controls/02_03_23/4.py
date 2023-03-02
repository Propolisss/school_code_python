minn = float('inf')

for i in range(1, 10_000_000):
    n = bin(i)[2:]
    temp_n = i
    temp_n -= n.count('0')
    n = bin(temp_n)[2:]
    n = n[-3:] + n
    if int(n, 2) > 224:
        minn = min(minn, int(n, 2))
print(minn)