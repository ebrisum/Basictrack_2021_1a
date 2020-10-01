import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()


square = 50

leonardo.shape("turtle")
leonardo.color("red", "green")
leonardo.speed(10)

while square>0:
    leonardo.forward(200)
    leonardo.left(90)
    leonardo.forward(200)
    leonardo.left(100)
    leonardo.forward(250)
    square -=1

for i in range(100):
    leonardo.speed(20)
    leonardo.forward(100)
    leonardo.right(50)
    leonardo.right(50)
    leonardo.forward(100)

leonardo.pendown()

paper.exitonclick()