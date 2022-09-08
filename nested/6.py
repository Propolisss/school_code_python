n = int(input())
num = 1
l = []

for i in range(1, n + 1):
    l = []
    for j in range(i):
        l.append(str(num))
        num += 1
    print(' '.join(l))