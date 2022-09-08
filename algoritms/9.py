maxx = 0


for i in range(1, 10000):
    N = i
    st = ''
    while N > 0:
        st += str(N % 6)
        N //= 6
    st = st[::-1]
    st += str(st[-1])
    st = int(st)
    stt = ''
    while st > 0:
        stt += str(st % 2)
        st //= 2
    stt = stt[::-1]
    stt += stt[-1]
    if int(stt, 2) < 344:
        if int(stt, 2) > maxx:
            maxx = int(stt, 2)
print(maxx)