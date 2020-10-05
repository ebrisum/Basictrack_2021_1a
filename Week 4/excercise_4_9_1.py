import turtle

def draw_squares(animal, size, squares):
    for i in range(squares):
        for x in range(4):
            animal.forward(size)
            animal.left(90)
        animal.penup()
        animal.forward(2*size)
        animal.pendown()

window = turtle.Screen()
warner = turtle.Turtle()
window.bgcolor("lightgreen")
draw_squares(warner, 10, 10)


window.exitonclick()

