


for i in range(100000):
    s1 = 0
    s2 = 0
    R = 0
    for j in range(len(str(i))):
        if int(str(i)[j]) % 2 != 0:
            s1 += int(str(i)[j])
        else:
            s1 += 0
    for k in range(1, len(str(i)), 2):
        s2 += int(str(i)[k])
    R = abs(s1 - s2)
    if R == 27:
        print(i)
        break