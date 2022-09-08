st = open('24-153.txt').readline()
count = 0
i = 0
stt = ''

while i < len(st):
    if st[i] == 'A':
        stt += st[i]
        i += 1
        if st[i] == 'F':
            continue
            i += 1
            stt = ''
        else:
            while st[i] != 'F':
                stt += st[i]
                i += 1
            stt += 'F'
            if 7 <= len(stt) <= 10:
                print(stt)
    if 7 <= len(stt) <= 10:
        count += 1
    else:
        i += 1
        stt = ''
print(count)
