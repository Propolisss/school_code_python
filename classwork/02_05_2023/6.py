st = open('24_1761.txt').readline()
maxx = 1
maxx_pal = ''

for i in range(1, len(st) - 1):
    curr_1 = 1
    curr_0 = 2
    if st[i] == st[i + 1]:
        maxx = max(maxx, curr_0)
        for j in range(1, i + 1):
                if i + j + 1 < len(st) and st[i - j] == st[i + j + 1]:
                    curr_0 += 2
                    maxx = max(maxx, curr_0)
                else:
                    break
    for j in range(1, i + 1):
            if i + j < len(st) and st[i - j] == st[i + j]:
                curr_1 += 2
                maxx = max(maxx, curr_1)
            else:
                break
print(maxx)