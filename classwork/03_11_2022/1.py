st = open('24-222.txt').readline().split('A')
#st = 'A11A11A11A11'.split('A')
maxx = 0
temp_st = ''



for i in range(len(st)):
    count = 1
    temp_st = ''
    for j in range(i + 1, len(st)):
        if st[j - 1] == st[j]:
            count += 1
            if count == 2:
                temp_st += st[i] + st[j]
            else:
                temp_st += st[j]
            if j == len(st) - 1:
                maxx = max(maxx, len(temp_st) + count)
            else:
                maxx = max(maxx, len(temp_st) + count + 1)
        else:
            if j == len(st) - 1:
                maxx = max(maxx, len(temp_st) + count)
            else:
                maxx = max(maxx, len(temp_st) + count + 1)
            count = 1
            break
print(maxx)
