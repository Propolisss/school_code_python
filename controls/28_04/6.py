st = open('24-1.txt').readline()
list = []
stt = ''
nums = '0123456789'
for i in range(len(st)):
    if st[i] in nums:
        if int(st[i]) % 2 == 0:
            stt += st[i]
        else:
            stt = ''
    else:
        list.append(stt)
        stt = ''
print(set(list))
