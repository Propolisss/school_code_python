summ = 0
st = ''
summ_2 = 0
count = 0

for i in range(1, 1000):
    st = ''
    st_2 = ''
    N = i
    summ = 0
    summ_2 = 0
    while N > 0:
        summ += N % 2
        st += str(N % 2)
        N //= 2
    st = st[::-1]
    while summ > 0:
        st_2 += str(summ % 2)
        summ //= 2
    st_2 = st_2[::-1]
    if i & 1:
        st += '00'
        st = '1' + st
    else:
        st += st_2
    if 500 <= int(st, 2) <= 700:
        count += 1
print(count)