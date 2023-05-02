st = open('24_1761.txt').readline()
maxx = float('-inf')

for i in range(1, len(st) - 1):
    curr_1 = 1
    curr_0 = 2
    if st[i] == st[i + 1]:
        for j in range(1, i + 1):
            if st[i - j] == st[i + j + 1]:
                curr_0 += 2
                maxx = max(maxx, curr_0)
            else:
                break
    else:
        for j in range(1, i):
            if st[i - j] == st[i + j]:
                curr_1 += 2
                maxx = max(maxx, curr_1)
            else:
                break
print(maxx)