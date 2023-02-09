for n in range(1, 100):
    st = '3' * 15 + '2' * 18 + '1' * n
    while '31' in st or '33' in st or '21' in st:
        if '31' in st:
            st = st.replace('31', '123', 1)
        if '33' in st:
            st = st.replace('33', '211', 1)
        if '21' in st:
            st = st.replace('21', '1', 1)
    if sum(int(i) for i in st) > 24:
        print(n)
        break