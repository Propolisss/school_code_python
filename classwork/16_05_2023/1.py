file = open('27B_7879.txt')
n = int(file.readline())
k = int(file.readline())
k47 = [float('-inf')] * 2023
n47 = [float('-inf')] * 2023
buff = []
maxx = float('-inf')

for i in range(k - 1):
    x = int(file.readline())
    buff.append(x)

for i in range(n - k):
    x = int(file.readline())
    ost = 0 if x % 2023 == 0 else 2023 - x % 2023
    if x % 47 == 0:
        maxx = max(maxx, n47[ost] + x)
    else:
        maxx = max(maxx, k47[ost] + x)

    if buff[0] % 47 == 0:
        k47[buff[0] % 2023] = max(k47[buff[0] % 2023], buff[0])
    else:
        n47[buff[0] % 2023] = max(n47[buff[0] % 2023], buff[0])
    buff.pop(0)
    buff.append(x)
print(maxx)