from turtle import *
tracer(0)
screensize(10000, 10000)
k = 1

for i in range(20):
    circle(4 * k)
    goto(xcor() + 8 * k, ycor() + 0)

goto(xcor() + 0, ycor() - 12)

for i in range(10):
    circle(8 * k)
    goto(xcor() - 16 * k, ycor() + 0)

goto(xcor() + 0, ycor() - 14 * k)

for i in range(15):
    circle(6 * k)
    goto(xcor() + 12 * k, ycor() + 0)


update()
exitonclick()