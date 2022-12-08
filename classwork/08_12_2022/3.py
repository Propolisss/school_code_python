



def f(n):
    if n <= 15:
        return n * n + 11
    elif n > 15 and (n % 2 == 0):
        return f(n // 2) + n * n * n - 5 * n
    if n > 15 and (n & 1):
        return f(n - 1) + 2 * n + 3

count = 0

for i in range(1, 1000 + 1):
    if str(f(i)).count('6') >= 3:
        count += 1
print(count)