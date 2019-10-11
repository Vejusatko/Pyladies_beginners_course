from turtle import forward, left, exitonclick

n = 59
side = 1
angle = 45

for i in range(n):
    left(angle)
    forward(side)
    
    side += 1

exitonclick()