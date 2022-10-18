from itertools import product

def is_gl(st):
    for i in range(1, len(st)):
        if st[i - 1] in gl and st[i] in gl:
            if ord(st[i - 1]) > ord(st[i]):
                return False
        if st[i - 1] in sogl and st[i] in gl:
            return False
    return True
def is_sogl(st):
    for i in range(1, len(st)):
        if st[i - 1] in sogl and st[i] in sogl:
            if ord(st[i - 1]) < ord(st[i]):
                return False
        if st[i - 1] in sogl and st[i] in gl:
            return False
    return True


sogl = 'BCD'
gl = 'AE'

s = list(map(''.join, product('ABCDE', repeat=4)))
count = 0

for i in range(len(s)):
    if (is_gl(s[i])) and (is_sogl(s[i])):
        count += 1
print(count)



