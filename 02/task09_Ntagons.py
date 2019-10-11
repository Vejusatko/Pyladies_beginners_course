from turtle import forward, left, penup, pendown, setposition, exitonclick
#move
penup()
setposition(-200.0,0.0)
pendown()
#draw for N
for i in [5,6,7,8]:
    #an N-shape
    for j in range(i):
        x = 200/i
        angle = 180 - (180 * (1 - 2/i))
        forward(x)
        left(angle)
    #move
    penup()
    forward(100)
    pendown()

exitonclick()