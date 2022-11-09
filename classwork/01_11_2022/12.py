



minn_len = 10 ** 10
minn_five = 10 ** 10

for i in range(251, 2000):
    st = '5' * i
    len_st = len(st)
    while '55555' in st:
        st = st.replace('55555', '88', 1)
        st = st.replace('888', '555', 1)
    if st.count('5') < minn_five:
        minn_five = st.count('5')
        minn_len = len_st
    if st.count('5') ==  minn_five:
        minn_len = min(minn_len, len_st)
print(minn_len)