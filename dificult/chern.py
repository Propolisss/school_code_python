d = 0
st = ''
last = 0

for i in range(1, 1000):
    summ = 0
    N = i
    d = 0
    st = ''
    last = 0
    while N > 0:
        last = N % 2
        st += str(last)
        N //= 2
    if i % 2 == 0:
        st += '01'
    else:
        st += '10'
    if int(st, 2) > 73:
        print(i)
        break