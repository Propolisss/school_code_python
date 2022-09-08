st = ''
last = 0

for i in range(1, 257):
    st = ''
    N = i
    nn = bin(N)
    nn = nn[2:]
    while len(nn) != 8:
        nn = '0' + nn
    last = nn.rfind('1')
    for j in range(8):
        if j == last:
            st += '1'
            while len(st) != 8:
                st += '0'
            break
        else:
            if int(nn[j]) == 1:
                st += '0'
            else:
                st += '1'
    num = int(st, 2)
    print(N, num)