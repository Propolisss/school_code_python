def f(a, b, count, target, st):
    if ((a >= 50) or (b >= 50)) and (a + b <= 109):
        if (count % 2) == (target % 2):
            return st
        else:
            return 0
    elif count == target: return 0
    h = [f(a + 1, b, count + 1, target, st + 'А'), f(a + 2, b, count + 1, target, st + 'Б'), f(a * 2, b, count + 1, target, st + 'В'), f(a, b + 1, count + 1, target, st + 'А'), f(a, b + 2, count + 1, target, st + 'Б'), f(a, b * 2, count + 1, target, st + 'В')]
    arr = []
    if (count + 1) % 2 == target % 2:
        flag = 0
        for i in h:
            if i:
                flag += 1
                arr.append(i)
    else:
        flag = 1
        for i in h:
            if i:
                arr.append(i[0])
            else:
                flag *= 0
    if flag > 0 and len(arr) > 0:
        return arr
    return 0

ans = []
for i in range(1, 49 + 1):
    if f(24, i, 0, 4, '') != 0:
        print(i, f(24, i, 0, 4, ''))
        ans.extend(f(24, i, 0, 4, ''))