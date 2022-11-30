st1 = [int(i) for i in input().split()]
st2 = [int(i) for i in input().split()]
print(*[st1[i] + st2[i] for i in range(len(st1))])
