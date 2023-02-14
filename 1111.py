from fnmatch import *

arr = [0, 0, 0, 0, 0]

for i in range(2023, 10 ** 10, 2023):
    if len(str(i)) > 9:
        break
    if i % 19 == 0 and i % 6 == 0 and len(str(i)) == 9:
        if fnmatch(str(i), '1*1*1?'):
            arr.append([i, i // 2023])
            arr.pop(0)
print(*arr, sep='\n')