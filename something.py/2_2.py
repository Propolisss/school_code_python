a, b, c = input().split()

if a == b == c:
    print('целых 3!')
elif a == b or a == c:
    print('парочка')
elif b == c:
    print('парочка')
else:
    print('0')