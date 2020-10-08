import turtle
window = turtle.Screen()
warner = turtle.Turtle()

def star(animal, size):
    for i in range(5):
        animal.forward(size)
        animal.right(144)

star(warner, 200)
window.exitonclick()




