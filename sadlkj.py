count = 0
num = 0

def simple(nn):
    for i in range(2, int(nn ** 0.5) + 1):
        if nn % i == 0:
            return False
    return True

for j in range(245690, 245756 + 1):
    num += 1
    if simple(j):
        print(num, j, sep = ' ')
