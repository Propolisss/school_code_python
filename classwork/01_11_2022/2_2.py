print('z w y x f')

for z in range(2):
    for w in range(2):
        for y in range(2):
            for x in range(2):
                f = z or ((w or (not y)) == (x <= z))
                if not f:
                    print(z, w, y, x, f)