st = open('24.txt').readline().replace('D', 'C').replace('F', 'C').replace('O', 'A')
maxx = float('-inf')
count = 0
i = 0

while i < len(st) - 2:
    if st[i] == 'C' and st[i + 2] == 'A':
        count += 1
        i += 3
    else:
        i += 1
        maxx = max(maxx, count)
        count = 0
print(maxx)