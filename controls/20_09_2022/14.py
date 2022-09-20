num = 3 * 256 ** 320 - 2 * 64 ** 290 + 4 ** 250 - 1023

st = ''
count = 0

while num:
    st += str(num % 4)
    num //= 4
st = st[::-1]

for i in range(len(st)):
    if st[i] != '0':
        count += 1
print(count, len(st), len(st) - st.count('0'))