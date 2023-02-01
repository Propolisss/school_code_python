file = open('1.txt')
maxx, n = map(int, file.readline().split())
nums = [int(i) for i in file]
nums.sort()

count = 0
summ = 0

for i in nums:
    if (summ + i) <= maxx:
        count += 1
        summ += i
    else:
        if (maxx - summ + i) in nums:
            print(count, (maxx - summ + i))
            break
