from fnmatch import *

for i in range(21, 10 ** 8 + 1, 21):
    if fnmatch(str(i), '1234*54'):
        print(i, i // 21)