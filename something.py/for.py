print('w', 'x', 'y', 'z', 'f')
for w in range (0,2):
    for x in range (0,2):
        for y in range (0,2):
            for z in range (0,2):
                f = x and not y and (not z or w)
                if f == 1:
                    print(w, x, y, z, f)