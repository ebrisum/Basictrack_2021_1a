import turtle
window = turtle.Screen()
warner = turtle.Turtle()

def star(animal, size):
    for i in range(5):
        animal.forward(size)
        animal.right(144)

for x in range(5):
    warner.penup()
    warner.forward(400)
    warner.right(144)
    warner.pendown()
    star(warner,120)

window.exitonclick()




