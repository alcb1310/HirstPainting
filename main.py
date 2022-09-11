from random import choice
from data import color_list
import turtle as t

t.colormode(255)
timmy = t.Turtle()
timmy.speed(0)

for _ in range(10):
    for _ in range(10):
        dot_color = choice(color_list)
        timmy.penup()
        timmy.dot(20, dot_color)
        timmy.fd(30)

    timmy.lt(90)
    timmy.fd(30)
    timmy.lt(90)
    timmy.fd(300)
    timmy.rt(180)


screen = t.Screen()
screen.exitonclick()
