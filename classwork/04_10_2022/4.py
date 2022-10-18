from itertools import *

s1 = list(map(''.join, product('ГОЛ', repeat=10)))
s2 = list(map(''.join, product('ГОЛ', repeat=10)))

count = 0

for i in range(len(s1)):
    for j in range(len(s2)):
        s = s1[i] + s2[j]
        if (s[0] != 'Г' and s[-1] != 'Г') and ('ОГО' not in s) and ('ЛГЛ' not in s) and ("ГГ" not in s) and ('ОО' not in s) and ('ЛЛ' not in s):
            count += 1
print(count)


