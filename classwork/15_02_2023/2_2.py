from itertools import *
p = set(range(1, 10 + 1))
q = {2, 4, 8, 10}
count = 0

def f(x):
    return ((x in q) <= (x in a)) and ((x in a) <= (x in p))

for i in range(20):
    for a in combinations(set(range(20)), i):
        if all(f(x) for x in range(1000)):
            count += 1
print(count)