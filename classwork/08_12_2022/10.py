fill = input()
base = int(input())

def draw_triangle(fill_, base_):
    for i in range(base_):
        if (i + 1) <= (base_ // 2) + 1:
            print(fill_ * (i + 1))
        else:
            print(fill_ * (base_ - i))
draw_triangle(fill, base)