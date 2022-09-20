from itertools import permutations

st = list(permutations("КУСАТЬ", 5))

ans = []
for i in range(len(st)):
    temp_st = ''
    for j in range(len(st[i])):
        temp_st += st[i][j]
    ans.append(temp_st)

print(ans)
count = 0
for i in range(len(ans)):
    if st[i][0] != 'Ь' and ('СУК' not in ans[i]):
        count += 1
print(count)
