from functools import lru_cache
fibs = []

@lru_cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(100): fibs.append(fib(i))
ans = set()
print(fibs)

for i in range(len(fibs)):
    for j in range(len(fibs)):
        for k in '0123456789':
            n = int(f'73{k}5{fibs[i]}486{fibs[j]}')
            if n % 43 == 0 and n <= 10 ** 9:
                ans.add(n)
        if int(f'735{fibs[i]}486{fibs[j]}') % 43 == 0 and int(f'735{fibs[i]}486{fibs[j]}') <= 10 ** 9:
            ans.add(int(f'735{fibs[i]}486{fibs[j]}'))

for i in sorted(ans):
    print(i, i // 43)