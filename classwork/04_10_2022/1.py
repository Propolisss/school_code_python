from itertools import *

s = list(map(''.join, product('ЕГЭИНФ', repeat=6)))
count = 0

for i in s:
    if (i[0] == 'Е') and (i[-1] == 'Э' or i[-1] == 'И') and (i.count('ФИ') >= 2) and ('ЕГЭ' not in i):
        count += 1
print(count)