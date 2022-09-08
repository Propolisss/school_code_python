maxx = 0
maxxx = 0

for i in range(200, 1000):
    st = '5' * i
    while '55555' in st:
        st = st.replace('55555', '88', 1)
        st = st.replace('888', '555', 1)
    if st.count('5') > maxx:
        maxx = st.count('5')
        maxxx = i
print(maxxx)
