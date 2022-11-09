from functools import lru_cache


def to_null(n):
    st = n[1:]
    st = st.replace('1', '0')
    return n[0] + st

def true_to_null(n):
    st = n[1:]
    st = st.replace('1', '0')
    if n[1:] == st:
        return False
    return True

@lru_cache
def f(start, end):
    if int(str(start), 2) < int(str(end), 2):
        return 0
    elif int(str(start), 2) == int(str(end), 2):
        return 1
    else:
        if true_to_null(str(start)):
            return f(bin(int(str(start), 2) - 1)[2:], end) + f(to_null(str(start)), end)
        else:
            return f(bin(int(str(start), 2) - 1)[2:], end)

print(f(1100, 100))