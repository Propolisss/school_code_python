st = open('24_3900.txt').readline().replace('A', ' A').split()
maxx = float('-inf')

for i in range(len(st) - 3):
    if st[i - 3] == st[i - 2] == st[i - 1]:
        maxx = max(maxx, len(st[i - 3]) + len(st[i - 2]) + len(st[i - 1]) + 1)
print(maxx)