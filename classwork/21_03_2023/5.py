file = open('26 (1).txt')

def find_minn(n_):
    for i in range(n):
        if not(flags[i]) and med[i] <= n_:
            return i
    return 'aaa'

def find_minn2():
    for i in range(n):
        if not(flags[i]):
            return i
    return 'aaa'


n = int(file.readline())
summ = 100_000
nums = sorted([int(i) for i in file])
flags = [0] * n
med = [i // 2 for i in nums]
count = 0

curr_summ = 0
red_ind = 0
red_summ = 0
red_arr = []

for i in range(len(nums)):
    red_summ += nums[i]
    red_arr.append(nums[i])
    if red_summ > summ:
        red_ind = i
        red_summ -= nums[i]
        del red_arr[-1]
        break
med = med[red_ind:]
maxx = float('-inf')
count = 0

while True:
    count_red = len(red_arr) // 6
    sale = sum(red_arr[-count_red:]) // 2
