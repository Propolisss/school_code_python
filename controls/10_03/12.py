z = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
l = []
st = ''

while z > 0:
    st += str(z % 15)
    z //= 15
st = st[::-1]
print(st)
for i in range(len(st)):
    if st[i] not in l:
        l.append(i)
print(l)