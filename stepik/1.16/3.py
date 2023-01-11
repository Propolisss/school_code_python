def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    return sorted([(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)])

print(*solve(int(input()), int(input()), int(input())))