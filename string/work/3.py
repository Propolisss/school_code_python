st = ''
maxx = 0
maxx_index = 0

for i in range(100, 1000):
    st = '1' * i
    while ('333' in st) or ('111' in st):
        st = st.replace('333', '11', 1)
        st = st.replace('111', '3', 1)
    if int(st) > maxx:
        maxx = int(st)
        if i > maxx_index:
            maxx_index = i
print(maxx_index)