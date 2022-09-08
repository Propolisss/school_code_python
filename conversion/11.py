s = input()
names = ''
i = 0

while s != '* !':
    names += s.title() + '*'
    s = input()

while i <= len(names):
    if names[i] == '*':
        if names[i - 1] == ' ':
            print(names[:i - 1])
        else:
            print(names[:i])
        names = names[i + 1:]
        i = 0
    i += 1