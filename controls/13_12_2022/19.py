


def f(vers, rebr, count, target, last, summ):
    if summ >= 70: return (count % 2) == (target % 2)
    if count == target: return 0
    h = []
    if count == 0:
        h.append(f(vers + 1, rebr + 2, count + 1, target, '+1vers2', summ + 4))
        h.append(f(vers + 1, rebr + 1, count + 1, target, '+1vers1', summ + 1))
    else:
        if last == '+1vers1':
            h.append(f(vers + 1, rebr + 2, count + 1, target, '+1vers2', summ + 4))
            h.append(f(vers, rebr - 1, count + 1, target, '-1rebr', summ - 2))
        elif last == '+1vers2':
            h.append(f(vers + 1, rebr + 1, count + 1, target, '+1vers1', summ + 1))
            h.append(f(vers, rebr - 1, count + 1, target, '-1rebr', summ - 2))
        elif last == '-1rebr':
            h.append(f(vers + 1, rebr + 2, count + 1, target, '+1vers2', summ + 4))
            h.append(f(vers + 1, rebr + 1, count + 1, target, '+1vers1', summ + 1))
        else:
            h.append(f(vers + 1, rebr + 2, count + 1, target, '+1vers2', summ + 4))
            h.append(f(vers + 1, rebr + 1, count + 1, target, '+1vers1', summ + 1))
            h.append(f(vers, rebr - 1, count + 1, target, '-1rebr', summ - 2))
    if (count + 1) == 3: return any(h)
    else:
        return any(h) if (count + 1) % 2 == target % 2 else all(h)

for s in range(3, 34 + 1):
    if (not(f(s, s, 0, 2, '0', 2 * s))) and (f(s, s, 0, 4, '0', 2 * s)):
        print(s)