st = input()
stt = ''

for i in range(len(st)):
    if i % 3 == 0:
        stt += ''
    else:
        stt += st[i]
print(stt)