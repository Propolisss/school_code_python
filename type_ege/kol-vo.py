a = int(input())
b = int(input())
count = 0

for i in range(a, b + 1):
    i **= 3
    if i % 10 == 4 or i % 10 == 9:
        count += 1
print(count)