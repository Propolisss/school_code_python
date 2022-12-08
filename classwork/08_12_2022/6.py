arr = ['КРУГОЗОР', 'КРУГОМ', 'КРУГООБОРОТ', 'КРУЖАЛО', 'КРУЖКА', 'МИНОГ', 'МИНОР', 'МИРАЖ', 'МИРАБИЛИТ']


def f(st, count, chet):
    if any(st == i for i in arr): return (count % 2) == chet
    h = []
    for i in range(len(arr)):
        if len(st) == 0:
            h.append(f(arr[i][0], count + 1, chet))
        elif st in arr[i]:
            h.append(f(st + arr[i][len(st)], count + 1, chet))
    print(h)
    return any(h) if (count + 1) % 2 == chet else all(h)

for i in arr:
    if i == 'МИНОР':
        print('111111')
    if f('', 0, 0):
        print(1)