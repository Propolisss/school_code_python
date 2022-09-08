st = input()
maxx = 0
maxx_symbol = ''

for i in range(len(st)):
    if st.count(st[i]) >= maxx:
        maxx = st.count(st[i])
        maxx_symbol = st[i]
print(maxx_symbol)