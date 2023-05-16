import time
timee = time.time()

file = open('27_B_6057.txt')
dic = [0]
n = int(file.readline())

for i in file:
    nums = [int(j) for j in i.split()]
    summs = [a + b for a in nums for b in dic]
    dic = {s % 91 : s for s in sorted(summs)}.values()
    #dic = {s % 91 : s for s in sorted([a + b for a in nums for b in dic])}.values()
print(max(i for i in dic if i % 91 != 0), time.time() - timee)