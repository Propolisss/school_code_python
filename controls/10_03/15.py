count = 0
maxx_count = 0
maxx_num = 0

for i in range(120115, 120200 + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count >= maxx_count:
        maxx_count = count
        if i > maxx_num:
            maxx_num = i
print(maxx_count, maxx_num, sep = '')