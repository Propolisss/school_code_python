strs = list(input().split())
ans = ''
maxx = 0

for i in range(len(strs)):
    maxx = max(maxx, len(strs[i]))

for i in range(maxx):
    temp = True
    for j in range(1, len(strs)):
        if i >= len(strs[j - 1]) or i >= len(strs[j]) or strs[j - 1][i] != strs[j][i]:
            temp = False
            break
    if not temp:
        break
    ans += strs[0][i]

if len(ans) != 0:
    print(ans)
else:
    print('хлеб')