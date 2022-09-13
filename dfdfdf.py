from itertools import product

st = 'АНДРЕЙ'
al = list(product(st, repeat=4))

print(al)
count = 0
for i in range(len(al)):
    if ('А' in al[i] or 'Е' in al[i]) and al[i][0] != 'Й':
        count += 1
print(count)