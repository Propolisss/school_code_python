st = '1900'


while '900' in st or '8000' in st or '70' in st:
    st = st.replace('8', '70', 1)
    st = st.replace('70', '900', 1)
    st = st.replace('900', '8000', 1)
    if len(st) == 71:
        break
print(len(st))