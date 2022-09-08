n = int(input())
l = []

for i in range(1, n + 1):
    l = []
    for j in range(5):
        l.append(str(i))
    print(' '.join(l))