import argparse
import turtle

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
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("order", type=int)
    return parser.parse_args()

def main():
    args = parse_arguments()
    draw_koch_curve(args.order)

if __name__ == "__main__":
    main()
