#n = int(input('Insert number of sides: ') )

from turtle import forward, left, exitonclick
from math import sqrt

n = int(input('Insert number of sides: ') )
x = 200/n
angle = 180 - (180 * (1 - 2/n))

for i in range(n):
    forward(x)
    left(angle)

exitonclick()