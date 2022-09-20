st = open('24.txt').readline()

i = 1
temp_st = ''
maxx = 0
previous_index = 0

while i < len(st):
    if st[i - 1] != st[i]:
        temp_st += st[i - 1] + st[i]
        i += 1
    else:
        previous_index += 1
        maxx = max(maxx, len(temp_st))
        temp_st = ''
        i = previous_index
print(maxx)