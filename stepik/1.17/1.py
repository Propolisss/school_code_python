def find_r(n):
    maxx = float('-inf')
    minn = float('inf')

    for j in range(len(str(i)) - 1):
        maxx = max(maxx, int(str(i)[j:j + 2]))
        minn = min(minn, int(str(i)[j:j + 2]))
    return maxx - minn

for i in range(10, 1_000_000):
    if find_r(i) == 44:
        print(i)
        break