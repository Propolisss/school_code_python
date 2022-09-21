st = open('24.txt').readline()

i = 1

temp_st = st[0]
maxx = 0
previous_index = 0

while i < len(st):
    if st[i - 1] != st[i]:
        temp_st += st[i]
        i += 1
    else:
        maxx = max(maxx, len(temp_st))
        previous_index += 1
        i = previous_index
        temp_st = st[i - 1]
print(maxx)