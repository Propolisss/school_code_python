s = input().split()
maxx = float('-inf')

for i in s:
    maxx = max(maxx, len(i))
print(maxx)