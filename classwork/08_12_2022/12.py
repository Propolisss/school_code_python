def print_digit_sum(num_):
    print(sum(int(i) for i in str(num_)))

num = int(input())
print_digit_sum(num)