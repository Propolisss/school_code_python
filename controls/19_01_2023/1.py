def unic(arr):
    return sorted(set(arr))

print(*unic([int(i) for i in input().split(',')]), sep=', ')