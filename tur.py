import turtle
myPen=turtle.Pen()
myPen.speed(0)
myPen.pensize(5)
myPen.color("red")
for i in range(20):
    for j in range(4):
        myPen.forward(50)
        myPen.right(90)
    myPen.penup()
    myPen.goto(70*i,0)
    myPen.pendown()
turtle.done()

