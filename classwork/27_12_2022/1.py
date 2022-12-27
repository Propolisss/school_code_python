# 20
# 7 19
# 6

def f(s, count, target, last):
    if s >= 62: return (count % 2) == (target % 2)
    if count == target: return 0
    h = []
    if last == '1':
        h.append(f(s + 2, count + 1, target, '2'))
        h.append(f(s * 3, count + 1, target, '3'))
    elif last == '2':
        h.append(f(s + 1, count + 1, target, '1'))
        h.append(f(s * 3, count + 1, target, '3'))
    elif last == '3':
        h.append(f(s + 1, count + 1, target, '1'))
        h.append(f(s + 2, count + 1, target, '2'))
    else:
        h.append(f(s + 1, count + 1, target, '1'))
        h.append(f(s + 2, count + 1, target, '2'))
        h.append(f(s * 3, count + 1, target, '3'))
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

for i in range(1, 61 + 1):
    if f(i, 0, 4, ''):
        print(i)