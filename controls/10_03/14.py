maxx = 0

for i in range(8388608, 838860800):
    x = i
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        if x % 2 != 0:
            b = b + 1
        x = x // 2
    if a == 25:
        print(i)
        break
print(maxx)