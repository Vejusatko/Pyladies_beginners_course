#Definition
def draw_house(side):
    from turtle import forward, left, right, exitonclick
    from math import sqrt
    #maths
    diagonal = sqrt(2*(side ** 2))
    #let's draw
    forward(side)
    left(135)
    forward(diagonal)
    right(135)
    forward(side)
    left(120)
    forward(side)
    left(120)
    forward(side)
    left(30)
    forward(side)
    left(135)
    forward(diagonal)
    right(135)
    forward(side)

draw_house(200)