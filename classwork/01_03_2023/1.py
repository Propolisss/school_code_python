from itertools import *

s = list(map(''.join, product('КОМПЬЮТЕР', repeat=6)))
ans = set()
cat = 'КОТ'

for i in s:
    ind = i.find('К')
    sr = i[ind:]
    ind2 = sr.find('О')
    sr2 = sr[ind2:]
    if 'Т' in (i[i.find('К'):])[i[i.find('К'):].find('О'):] and 'О' in i[i.find('К'):]:
        ans.add(i)

print(len(ans))