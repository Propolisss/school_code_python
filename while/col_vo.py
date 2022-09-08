count = 0
n = input()

while n != 'стоп' and n != 'хватит' and n != 'достаточно':
    count += 1
    n = input()
print(count)