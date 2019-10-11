from turtle import forward, left, exitonclick

n = 95
x = 200/n
angle = 180 - (180 * (1 - 2/n))

for i in range(n):
    forward(x)
    left(angle)

exitonclick()