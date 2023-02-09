ans = set()

for n in range(101, 1_000):
    st = '3' * n

    while '111' in st or '333' in st:
        if '111' in st:
            st = st.replace('111', '3', 1)
        else:
            st = st.replace('333', '1', 1)
    if st == '1':
        print(n)
        break