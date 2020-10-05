import turtle
size = 10
def draw_squares(animal, size, squares):
    for i in range(squares):
        for x in range(4):
            animal.forward(size)
            animal.left(90)
        size += 20
        animal.right(135)
        animal.penup()
        animal.forward(14)
        animal.left(135)
        animal.pendown()

window = turtle.Screen()
warner = turtle.Turtle()
window.bgcolor("lightgreen")
draw_squares(warner, 10, 10)


window.exitonclick()