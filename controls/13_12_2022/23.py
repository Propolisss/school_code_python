ans = set()

def f(start):
    if start > 100:
        return 0
    elif start < 100:
        if (start & 1):
            ans.add(start)
        f(start + 3)
        f(start * 3)
f(1)
print(len(ans), ans)

