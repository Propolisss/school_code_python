minn = 10 ** 100

for i in range(1000, 10000):
    st = str(i)
    while len(st) != 71:
        st += '0'
    while ('70' in st) or ('8000' in st) or ('900' in st):
        st = st.replace('70', '8', 1)
        st = st.replace('900', '70', 1)
        st = st.replace('8000', '900', 1)
        if len(st) == 4:
            if int(st) < minn:
                minn = int(st)
            break
print(minn)