file = open('9.txt')
nums = [[int(j) for j in i.split()] for i in file]
count = 0

for i in nums:
    rep = []
    no_rep = []

    for j in i:
        if i.count(j) == 1:
            no_rep.append(j)
        else:
            rep.append(j)

    if len(rep) == 3:
        if (sum(no_rep) / len(no_rep)) < sum(rep):
            count += 1
print(count)