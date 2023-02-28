def all_chet(n):
    temp_st = ''

    for i in str(n):
        n_ = '0' * (4 - len(bin(int(i))[2:])) + bin(int(i))[2:]
        n_ += str(n_.count('1') % 2)
        temp_st += n_
    temp_st = '1' + temp_st[2:] + '0'
    return temp_st

for i in range(1, 1_000_000):
    n = all_chet(i)
    if int(n, 2) == 674890:
        print(i)
        break