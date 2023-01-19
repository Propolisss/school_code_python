file = open('27B.txt')
n = int(file.readline())
dic = {}

for i in range(n):
    num = int(file.readline())
    if str(num)[0] in dic:
        dic[str(num)[0]] += 1
    else:
        dic[str(num)[0]] = 1
print(min(dic.values()))