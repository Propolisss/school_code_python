count = 0
st = ''
n = 0

for i in range(7 ** 6, 7 ** 7):
    st = ''
    n = i
    while n > 0:
        st += str(n % 7)
        n //= 7
    st = st[::-1]
    if st[0] != '3' and st[0] != '5' and st[0] != '0':
        if ((st.find('22') == -1) or (st.find('44') == -1)):
            count += 1
print(count)