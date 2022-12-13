st = '>' + '1' * 28 + '2' * 18 + '3' * 35

while ('>1' in st) or ('>2' in st) or ('>3' in st):
    if '>1' in st:
        st = st.replace('>1', '22>', 1)
    if '>2' in st:
        st = st.replace('>2', '2>1', 1)
    if '>3' in st:
        st = st.replace('>3', '1>2', 1)
#s = st.replace('>', '')
print(sum(int(i) for i in str(st[:-1])))