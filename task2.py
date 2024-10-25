import turtle
import sys

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size)
    t.pendown()

    for angle in [60, 60, 60, 60, 60, 0]:
        koch_curve(t, order, size)
        t.right(angle)

    window.mainloop()

if __name__ == '__main__':
    draw_koch_curve(int(sys.argv[1]))
