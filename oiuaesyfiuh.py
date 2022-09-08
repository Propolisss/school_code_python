count = 0
maxx = 0


def simple(nn):
    for i in range(2, int(nn ** 0.5) + 1):
        if nn % i == 0:
            return False
    return True

for j in range(154029, 154043 + 1):
    count = 0
    maax = 0
    maxx = 0
    for k in range(2, int(j ** 0.5) + 1):
        if j % k == 0:
            if simple(k):
                count += 1
                if k > maxx:
                    maxx = k
            if simple(j // k):
                count += 1
                if j // k > maxx:
                    maxx = j // k
    if count == 2:
        print(maxx, j)