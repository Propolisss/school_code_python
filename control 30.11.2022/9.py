m2 = []
n5 = []
ans = []

for m in range(1, 101 + 1, 2):
    m2.append(m)

for n in range(0, 10 + 1, 2):
    n5.append(n)

for i in range(len(m2)):
    for j in range(len(n5)):
        num = (2 ** m2[i]) * (5 ** n5[j])
        if 100_000_000 <= num <= 300_000_000:
            ans.append([num, m2[i] + n5[j]])
ans.sort()
print(*ans, sep='\n')