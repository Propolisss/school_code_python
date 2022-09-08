m = float(input())
p = float(input())
n = int(input())
p = p / 100 + 1

for i in range(1, n + 1):
    print(i, m)    
    m *= p