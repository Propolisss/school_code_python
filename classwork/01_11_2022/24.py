st = open('24.txt').readline()
count = 0

for i in range(3, len(st)):
    if st[i - 3:i + 1] == 'XXXX':
        count += 1
print(count)