p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
a = set(range(1, 1000))

def f(x):
    return ((x in a) <= (x in p)) or ((x not in q) <= (x not in a))

for x in range(1000):
    if not f(x):
        a.remove(x)
print(a)