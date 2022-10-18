s = input().split()
s[-1] = int(s[-1])

if len(s[0]) == 1:
    print(s[0])

strs = []

for i in range(len(s[0])):
    strs.append('')
ans = ''
flag = True
counter = 0

for i in range(len(s[0])):
    if flag:
        strs[counter] += s[0][i]
        counter += 1
    if not flag:
        strs[counter] += s[0][i]
        counter -= 1
    if (counter == s[1] - 1) or counter == 0:
        flag = not flag

for i in strs:
    ans += i

print(ans)