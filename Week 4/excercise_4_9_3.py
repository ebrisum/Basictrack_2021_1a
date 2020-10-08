import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

window = turtle.Screen()
warner = turtle.Turtle()
draw_poly(warner, 3, 100)
window.exitonclick()


