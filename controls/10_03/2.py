print('x', 'w', 'y', 'z', 'f')
for x in range(2):
    for w in range(2):
        for y in range(2):
            for z in range(2):
                f = ((x <= w) or y and (not z)) and ((y <= (not z)) or x and (not w))
                if f == 0:
                    print(x, w, y, z, f)