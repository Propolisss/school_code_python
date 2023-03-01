count = 0

for i in range(1_000_000, 9_999_999 + 1):
    st = str(i)
    if int(st[1:3]) == int(st[0]) ** 2 and (int(st[-2]) == int(st[-1]) ** 3 or int(st[-4:-1]) == int(st[-1]) ** 3 or int(st[-3:-1]) == int(st[-1]) ** 3):
        count += 1
        print(i, count)
print(count)