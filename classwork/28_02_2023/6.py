ans = set()

for n in range(1, 10000):
    for m in range(1, 10000):
        s_n = sum(int(j) for j in bin(n)[2:]) ** 2
        s_m = sum(int(j) for j in bin(m)[2:]) ** 2
        if s_n - s_m == 33:
            ans.add(n + m)
print(min(ans))