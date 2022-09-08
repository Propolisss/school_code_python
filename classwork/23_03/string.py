file = open('24-171.txt')
maxx = 0

for i in file:
    st = file.readline()
    count = 0
    lenn = 2
    while lenn < int(len(st)):
        if st[lenn - 2:lenn + 1] == 'XYZ':
            count += 3
            lenn += 3
            if count > maxx:
                maxx = count
        else:
            count = 0
            lenn += 1
print(maxx)
