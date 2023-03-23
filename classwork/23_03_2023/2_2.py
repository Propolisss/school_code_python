file = open('26_476.txt')
n = int(file.readline())
nums = sorted([int(i) for i in file])
all_summ = int(sum(nums) * 0.6)
count_rich = int(len(nums) * 0.2)
summ_rich = int(sum(nums[-count_rich:]) * 0.8)

for i in range(10, 100):
    summ_poor = int(sum(nums[:-count_rich]) * float(f'0.{i}'))
    if summ_poor + summ_rich <= all_summ:
        print(summ_rich, int(nums[0] * float(f'0.{i}')))