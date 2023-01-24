st = open('24.txt').readline()

dic = dict()

for i in range(1, len(st)):
    if st[i - 1] == 'A':
        if st[i] in dic:
            dic[st[i]] += 1
        else:
            dic[st[i]] = 1

maxx = max(dic.values())

for i in dic:
    if dic[i] == maxx:
        print(i, maxx, sep='')