maxx = float('-inf')

for i in range(1, 10_000):
    n1 = '0' * (8 - len(bin(i)[2:])) + bin(i)[2:]
    if len(n1) == 8:
        n2 = n1[::-1]
        r = abs(int(n1, 2) - int(n2, 2))
        maxx = max(maxx, r)

s1 = '11111111'
s2 = '00000001'
print(abs(int(s1, 2) - int(s2, 2)))
print(maxx)