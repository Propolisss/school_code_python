st = input()
count = 0

for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        count += 1
print(count)