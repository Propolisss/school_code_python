
def div(n):
    dels_ = set()

    for i in range(10, 100):
        if n % i == 0:
            dels_.add(i)
        if len(dels_) > 35:
            return {0}
    return dels_



for i in range(333555, 777999 + 1):
    dels = div(i)
    if len(dels) == 35:
        print(min(dels), max(dels))