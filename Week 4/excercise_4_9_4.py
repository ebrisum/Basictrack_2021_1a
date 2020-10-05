import turtle

def draw_square(animal, size, squares):
    for x in range(squares):
        for i in range(4):
            animal.forward(size)
            animal.left(90)
        animal.left(20)

window = turtle.Screen()
warner = turtle.Turtle()
warner.speed(100)
draw_square(warner, 100, 50)
window.exitonclick()
