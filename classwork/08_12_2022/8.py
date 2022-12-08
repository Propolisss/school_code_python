def draw_box():
    for i in range(14):
        st = ''
        for j in range(10):
            if i == 0 or i == 13:
                st += '*'
            elif j == 0 or j == 9:
                st += '*'
            else: st += ' '
        print(st)

draw_box()