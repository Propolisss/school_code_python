from fnmatch import *
from itertools import *
# s1 = list(map(''.join, product('0123456789', repeat=1)))
# s2 = list(map(''.join, product('0123456789', repeat=2)))
# s3 = list(map(''.join, product('0123456789', repeat=3)))
# s = []
# s.extend(s1)
# s.extend(s2)
# s.extend(s3)
# s += ['']
# s.sort()
# print(s)
#
# for i in s:
#     for j in '0123456789':
#         st = f'123{i}567{j}'
#         if int(st) % 169 == 0 and int(st) <= 10 ** 9:
#             print(int(st), int(st) // 169)

for i in range(0, 10 ** 9 + 2, 169):
     if fnmatch(str(i), '123*567?'):
         print(i, i // 169)