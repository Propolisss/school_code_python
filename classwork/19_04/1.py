st = '7' * 2022

while '777' in st or '333' in st:
    st = st.replace('777', '3', 1)
    st = st.replace('333', '7', 1)
print(st)