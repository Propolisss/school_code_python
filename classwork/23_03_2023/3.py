from datetime import *
start_time = datetime.now()

file = open('26_1257.txt')

n = int(file.readline())
ch = []
nech = []
ans = set()
for i in file:
    if int(i) & 1:
        nech.append(int(i))
    else:
        ch.append(int(i))
    ans.add(int(i))

maxx = float('-inf')
count = 0

for i in ch:
    for j in nech:
        if (i + j) in ans:
            maxx = max(maxx, i + j)
            count += 1
print(count, maxx, datetime.now() - start_time)