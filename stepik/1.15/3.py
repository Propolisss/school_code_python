def is_prime(num):
    return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def get_next_prime(num):
    flag = False
    i = num + 1
    while not flag:
        if is_prime(i):
            flag = True
        else:
            i += 1
    return i


print(get_next_prime(int(input())))