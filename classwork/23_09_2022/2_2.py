a = 'ababbababbaa'
q = 1
i = 1

while q < 4:
    c = a[i + 1]
    if (q == 2):
        if (c == 'a'):
            a = a[:i] + 'b' + a[i + 1:]
        else:
            q = 1
    if (q == 3):
        if (c == 'b'):
            a = a[:i] + 'a' + a[i + 1:]
        else:
            q = 1
    if (q == 1):
        a = a[:i] + a[i + 1:]
        i -= 1
        if c == 'a':
            q = 3
        if c == 'b':
            q = 2
    i += 1
    if i > len(a):
        q = 4
print(a)