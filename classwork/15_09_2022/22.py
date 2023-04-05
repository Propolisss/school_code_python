
for a in range(1, 10000):
    for x in range(15):
        for y in range(15):
            m = f'2{int(str(y), 15)}23{int(str(x), 15)}5'
            n = f'67{int(str(x), 13)}9{int(str(y), 13)}'
            if ((int(int(m, 15)) + a) % int(int(n, 13)) == 0):
                print(a)
                break