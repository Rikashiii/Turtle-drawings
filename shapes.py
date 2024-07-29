
import random
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.home()
tim.seth(0)
color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for sides in range(3, 11):
    angle = (360/sides)
    tim.pencolor(random.choice(color))
    for _ in range(sides):
        tim.right(angle)
        tim.forward(50)


t.exitonclick()
