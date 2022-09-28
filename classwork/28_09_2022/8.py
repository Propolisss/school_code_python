n = int(input())
st = ''
s = []

for i in range(n):
    s.append(input())
k = int(input())

for i in range(len(s)):
    if k < len(s[i]):
        st += s[i][k]
print(st)