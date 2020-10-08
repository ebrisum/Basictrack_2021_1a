import turtle
def spiral(animal, size):
    size = 100
    while size>0:
        size -= 10
        for i in range(2):
            animal.left(90)
            animal.forward(size)

window = turtle.Screen()
warner = turtle.Turtle()
spiral(warner, 100)
window.exitonclick()

