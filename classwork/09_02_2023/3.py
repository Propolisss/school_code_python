st = '5' * 12 + '4' * 23 + '53' * 17
while '43' in st or '53' in st:
    if '43' in st:
        st = st.replace('43', '33', 1)
    else:
        st = st.replace('53', '433', 1)
print(st.count('3'))