maxx = float('-inf')
maxx_len = float('-inf')

for i in range(301, 1_000):
    st = '5' * i
    while '55555' in st:
        st = st.replace('55555', '88', 1)
        st = st.replace('888', '55', 1)
    if st.count('5') > maxx:
        maxx = st.count('5')
        maxx_len = i
print(maxx_len)