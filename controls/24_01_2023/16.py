

def f(x, y):
    if y == 0:
        return x
    else:
        return f(y, x % y)

count = 0

for i in range(1, 1000 + 1):
    if f(i, 48) == 1:
        count += 1
print(count)