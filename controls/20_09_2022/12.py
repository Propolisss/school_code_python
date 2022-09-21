st = '1' + '8' + '0' * 69


while '900' in st or '8000' in st or '70' in st:
    st = st.replace('70', '8', 1)
    st = st.replace('900', '70', 1)
    st = st.replace('8000', '900', 1)
print(st)