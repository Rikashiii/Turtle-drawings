import turtle as t
from colours import color
import random

tim = t.Turtle()

tim.seth(0)
for _ in range(72):
    tim.speed(20)
    tim.color(random.choice(color))
    tim.circle(100)
    tim.right(5)

t.exitonclick()
