

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
for _ in range(50):
    tim.penup()
    tim.forward(4)
    tim.pendown()
    tim.forward(4)
t.exitonclick()



