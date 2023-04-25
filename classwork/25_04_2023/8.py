from itertools import *
s = [0] + list(map(''.join, product('АИМРЯ', repeat=4)))
print(s[211])