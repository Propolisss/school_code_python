def f(start, end, arr, flag):
    if (sum(arr) % 11 == 0) and (sum(arr) >= 11):
        flag = 1
    if start > end:
        return 0
    elif start == end and flag:
        return 1
    else:
        return f(start + 2, end, arr[1:] + [start], flag) + f(start * 3, end, arr[1:] + [start], flag) + f(start * 4, end, arr[1:] + [start], flag)

nums = [0, 0, 0]
print(f(1, 600, nums, 0))