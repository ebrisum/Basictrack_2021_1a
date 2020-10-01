import turtle


def draw_square(animal, size):
    for i in range(4):
        animal.forward(size)
        animal.left(90)

screen= turtle.Screen()
nick = turtle.Turtle()
nick.speed(200)

for index in range(60):
    draw_square(nick, index * 6)
    nick.left(6)

screen.exitonclick()