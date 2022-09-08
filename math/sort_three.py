a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) > a > min(a, b, c):
    print(max(a, b, c), a, min(a, b, c))
elif max(a, b, c) > b > min(a, b, c):
    print(max(a, b, c), b, min(a, b, c))
elif max(a, b, c) > c > min(a, b, c):
    print(max(a, b, c), c, min(a, b, c))