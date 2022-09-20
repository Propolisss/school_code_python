from turtle import *
tracer(0)

for i in range(15):
    goto(xcor() + 10 * 10, ycor() + 10 * 10)
    goto(xcor() + 3 * 10, ycor() - 6 * 10)
    goto(xcor() - 9 * 10, ycor() + 3 * 10)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * 10, y * 10)
        dot(5, "blue")
update()