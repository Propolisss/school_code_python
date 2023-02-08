st = open('24-180.txt').readline()
count = 0
maxx = float('-inf')

for j in range(len(st)):
    i = j
    while i < len(st) - 1:
        if 0 <= int(st[i : i + 4]) <= 2359:
            i += 4
            count += 4
        else:
            i += 1
            maxx = max(maxx, count)
            count = 0
            break
maxx = max(maxx, count)
print(maxx // 4)