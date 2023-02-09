st = '23' * 30 + '1' * 30

while '21' in st or '23' in st:
    if '21' in st:
        st = st.replace('21', '11', 1)
    else:
        st = st.replace('23', '21', 1)
print(st.count('1'))