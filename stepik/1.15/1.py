def is_valid_triangle(side1, side2, side3):
    return (max(side1, side2, side3) < ((side1 + side2 + side3) - max(side1, side2, side3)))

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(is_valid_triangle(n1, n2, n3))