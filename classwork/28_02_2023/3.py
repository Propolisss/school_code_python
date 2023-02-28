for i in range(1, 1_000_000):
    n = hex(i)[2:]
    if i % 2 == 0:
        n += 'f'
    else:
        n += '0'
    for _ in range(2):
        n += hex(sum(int(j, 16) for j in n) % 16)[2:]
    if n.count(hex(max(int(j, 16) for j in n))[2:]) / n.count(hex(min(int(j, 16) for j in n))[2:]) == 5:
        print(i)
        break