N = 0
st = ''

for i in range(96, 1000):
    N = i
    N = bin(i)
    st = N[2:]
    if st.count('0') == st.count('1'):
        st += st[len(st) - 1]
    else:
        if st.count('0') < st.count('1'):
            st += '0'
        else:
            st += '1'
    if st.count('0') == st.count('1'):
        st += st[len(st) - 1]
    else:
        if st.count('0') < st.count('1'):
            st += '0'
        else:
            st += '1'
    if st.count('0') == st.count('1'):
        st += st[len(st) - 1]
    else:
        if st.count('0') < st.count('1'):
            st += '0'
        else:
            st += '1'
    if int(st, 2) % 4 == 0:
        print(i)
        break