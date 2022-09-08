s = input()
count = 0
liter = 'йцукенгшщзхъфывапролджэячсмитьбю'

for i in range(len(s)):
    if s[i] in liter:
        count += 1
print(count)