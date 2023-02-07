file = open('27-49b.txt')
n = int(file.readline())
ost = []
summ = 0
all_ch = []
ch = [0, 0]

for i in file:
    nums = [int(j) for j in i.split()]
    ost.append(abs(nums[0] - nums[1]))
    all_ch.append(min(nums) % 2)
    summ += min(nums)
    ch[min(nums) % 2] += 1
ost.sort()


if (summ % 2 == ch.index(max(ch)) % 2):
    print(summ)
else:
    for i in range(len(ost)):
        if all_ch[i] & 1:
            if ost[i] % 2 == 0:
               continue
            else:
                ch[0] += 1
                ch[1] -= 1
                summ += ost[i]
                if (summ % 2 == ch.index(max(ch)) % 2):
                    print(summ)
                    break
        else:
            if ost[i] % 2 == 0:
                continue
            else:
                ch[1] += 1
                ch[0] -= 1
                summ += ost[i]
                if (summ % 2 == ch.index(max(ch)) % 2):
                    print(summ)
                    break