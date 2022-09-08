N = 0
st = ''
maxx = 0

for i in range(10000):
    N = i
    st = hex(N // 2)
    st = st[2:]
    if N % 4 == 0:
        st += 'C'
        st = st[0:0] + '15' + st[::]
    else:
        st += 'A0'
        st = st[0:0] + 'F' + st[::]        
    if int(st, 16) > maxx:
        maxx = i
print(maxx)