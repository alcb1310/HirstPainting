import turtle
from random import choice
from data import color_list
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
for _ in range(10):
    tim.fd(30)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        dot_color = choice(color_list)
        tim.dot(20, dot_color)
        tim.fd(30)

    tim.lt(90)
    tim.fd(30)
    tim.lt(90)
    tim.fd(300)
    tim.rt(180)

screen = t.Screen()
screen.exitonclick()
