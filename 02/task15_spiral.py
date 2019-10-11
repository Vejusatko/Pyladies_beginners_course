from turtle import forward, left, exitonclick

n = 1000
side = 1
angle = 10

for i in range(n):
    left(angle)
    forward(side)
    
    side += 0.1

exitonclick()