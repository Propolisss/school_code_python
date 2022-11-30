from fnmatch import *
st = input()

if fnmatch(st, '[0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]') or fnmatch(st, '7-[0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]'):
    print('YES')
else:
    print('NO')

# if (st[:3].isdigit() and (st[3] == '-') and st[4:7].isdigit() and (st[7] == '-') and st[-4:].isdigit()) or ((st[:3] == '7-') and st[2:5].isdigit() and (st[5] == '-') and st[6:9].isdigit() and (st[9] == '-') and st[-4:].isdigit()):
#     print('YES')
# else:
#     print('NO')