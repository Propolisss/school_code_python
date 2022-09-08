n = int(input())
max1 = 0
max2 = 0

for i in range(n):
    nn = int(input())
    if nn > max1:
        max2 = max1
        max1 = nn
    if nn > max2 and nn < max1:
        max2 = nn
print(max1, max2, sep = '\n')