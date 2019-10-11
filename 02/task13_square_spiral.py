from turtle import forward, left, exitonclick

n = 19
side = 5
angle = 90

for i in range(n):
    left(angle)
    forward(side)
    
    side += 5

exitonclick()