def f(n):
    st = ''

    for i in str(n):
        st += ('0' * (4 - len(bin(int(i))[2:]))) + bin(int(i))[2:]
    st = st.replace('0', '2').replace('1', '0').replace('2', '1')

    return st

for i in range(10, 99 + 1):
    if int(f(i), 2) == 151:
        print(i)