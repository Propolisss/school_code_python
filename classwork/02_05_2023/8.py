st = open('24_7016.txt').readline().replace('A', ' A').replace('D', ' D').split()
maxx = float('-inf')

for i in range(len(st) - 1):
    if st[i][0] != st[i + 1][0]:
        maxx = max(maxx, len(st[i]) + 1)
print(maxx)