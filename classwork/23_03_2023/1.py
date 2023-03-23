file = open('26_2944.txt')
summ, n = map(int, file.readline().split())
nums = sorted([int(i) for i in file])

curr_summ = 0
count = 0
for i in nums:
    if curr_summ + i <= summ:
        count += 1
        curr_summ += i
        last = i
    else:
        curr_summ -= last
        break

for i in nums[::-1]:
    if curr_summ + i <= summ:
        print(count, i)
        break