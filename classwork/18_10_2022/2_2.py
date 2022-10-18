from itertools import *
count = 0

for a in product('ВКНСТ', 'АВИКНСТ', 'АВИКНСТ', 'АИ'):
    count += 1
    st = ''.join(a)
    if st == 'НИКА':
        print(count)