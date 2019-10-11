from turtle import forward, left,  right, exitonclick
from math import sqrt

#house variables
x = 100
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
#exit
exitonclick()