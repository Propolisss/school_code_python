from turtle import *
tracer(0)
left(90)
k = 40

for i in range(8):
    for j in range(4):
        fd(5 * k)
        right(30)
        fd(6 * k)
        right(150)
    right(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3, "blue")


update()
exitonclick()