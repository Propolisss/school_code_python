def simple(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


for n in range(100):
    st = '>' + '1' * 16 + '2' * n + '3' * 16
    while '>1' in st or '>3' in st or '>2' in st:
        if '>1' in st:
            st = st.replace('>1', '1>', 1)
        if '>3' in st:
            st = st.replace('>3', '>2', 1)
        if '>2' in st:
            st = st.replace('>2', '>1', 1)
    st = st.replace('>', '')
    if simple(sum(int(i) for i in st)):
        print(n)
        break