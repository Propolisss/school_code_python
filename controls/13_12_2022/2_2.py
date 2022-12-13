print('x y w z f')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(x <= y)) or ((not(w)) <= (not(z))) or w
                if not f:
                    print(x, y, w, z, f)