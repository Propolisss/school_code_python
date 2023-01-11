from math import pi

def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2

print(*get_circle(float(input())))