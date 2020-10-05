import turtle


def draw_square(animal, size):
    for i in range(4):
        animal.forward(size)
        animal.left(90)

def calculate_surface(side_length):
    surface = side_length ** 2
    print(surface)
    return surface

screen= turtle.Screen()
nick = turtle.Turtle()
nick.speed(200)

for index in range(6):
    draw_square(nick, index * 6)
    nick.left(6)

    result = calculate_surface(index*6)
    print(result)
    
screen.exitonclick()