n = int(input())
st = ''

for i in range(1, n + 1):
    st = ''
    for j in range(1, i + 1):
        st += str(j)
    if i > 1:
        for k in range(i - 1, 0, -1):
            st += str(k)
    print(st)
        