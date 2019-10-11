from turtle import forward, left, right, exitonclick

# 18-times:
for i in range(18):

    # draw square
    for j in range(4):
        forward(50)
        left(90)

    # turn by 20°
    left(20)

exitonclick()