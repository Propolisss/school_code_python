x = int(input())
n = int(input())
st = ''

while x > 0:
    st += str(x % n)
    x //= n
st = st[::-1]
print(st)