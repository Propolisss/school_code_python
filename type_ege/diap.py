delit = 2
count = 0
d = 0

for i in range(174457,174506):
    for j in range(i):
        if i & j == 0:
            d = j
            count += 1
    if count == 2:
        print(d)