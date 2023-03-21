file = open('26 (1).txt')

n = int(file.readline())
summ = 100_000
nums = sorted([int(i) for i in file])

red_arr = []
maxx = float('-inf')
maxx2 = float('-inf')

for i in range(len(nums)):
    red_arr.append(nums[i])
    sale = len(red_arr) // 6
    if (sum(red_arr[:-sale]) + (sum(red_arr[-sale:]) // 2)) <= 100_000:
        maxx = max(maxx, len(red_arr))
        maxx2 = 100_000 - (sum(red_arr[:-sale]) + (sum(red_arr[-sale:]) // 2))
        print(maxx, maxx2)
print(maxx, maxx2)