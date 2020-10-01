import turtle
from datetime import datetime

now = datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
window = turtle.Screen()
warner = turtle.Turtle()
move = 30

warner.speed(100)
warner.shape("turtle")

for i in range(12):
    warner.penup()
    warner.forward(250)
    warner.pendown()
    warner.forward(10)
    warner.penup()
    warner.forward(30)
    warner.stamp()
    warner.home()
    warner.right(move)
    move=move+30

warner.pendown()
warner.pencolor("red")
warner.right(30*hour-90)
warner.pensize(10)
warner.forward(190)
warner.backward(190)
warner.left(30*hour-60)
warner.right(6*minute-60)
warner.pensize(5)
warner.forward(240)
warner.backward(240)


window.exitonclick()

