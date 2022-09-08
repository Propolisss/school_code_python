z = 16 ** 23 + 4 ** 12 - 32 ** 6
st = ''

while z > 0:
    st += str(z % 4)
    z //= 4
st = st[::-1]
print(st.count('3'))