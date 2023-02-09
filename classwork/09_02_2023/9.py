

for n in range(1, 1_000):
    st = '0' * n + '1'

    while '01' in st:
        if '1' in st:
            st = st.replace('1', '10', 1)
        if '01' in st:
            st = st.replace('01', '1000', 1)
    if 100 <= st.count('0') <= 999:
        print(n)
        break