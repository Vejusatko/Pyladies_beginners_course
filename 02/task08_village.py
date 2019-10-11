from turtle import forward, left,  right, penup, pendown, setposition, exitonclick
from math import sqrt
#move
penup()
setposition(-200.0,0.0)
pendown()
houses = 7
#village
for i in range(houses):
    #variables
    x = 50
    diagonal = sqrt(2*(x**2))
    #let's draw
    forward(x)
    left(135)
    forward(diagonal)
    right(135)
    forward(x)
    left(120)
    forward(x)
    left(120)
    forward(x)
    left(30)
    forward(x)
    left(135)
    forward(diagonal)
    right(135)
    forward(x)
    left(90)
    forward(20)

exitonclick()