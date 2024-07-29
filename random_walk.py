import turtle as t
import random
from colours import color

tim = t.Turtle()
tim.pensize(12)                                   #change line width
tim.speed(8)                                      #change the speed of turtle

for _ in range(100):
    tim.pencolor(random.choice(color))
    tim.forward(25)
    tim.seth(random.choice([90, 180, 270, 360]))

t.exitonclick()
