from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20

for i in range(10):
    goto(xcor() + 3, ycor() - 4)
    dot(4, 'blue')
    goto(xcor() - 7, ycor() + 24)
    dot(4, 'blue')
    goto(xcor() + 12, ycor() + 5)
    dot(4, 'blue')



update()
exitonclick()