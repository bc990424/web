import turtle
from math import sin


def add_mouse_listener():
    def on_motion(event):
        nonlocal x, y
        x = event.x - turtle.window_width() / 2
        y = -event.y + turtle.window_height() / 2

    turtle.getcanvas().bind("<Motion>", on_motion)
    x, y = 0, 0
    return lambda: (x, y)


def color(c, a):
    return sin(c + a) / 2 + 0.5


def colors(r, ra, g, ga, b, ba):
    return color(r, ra), color(g, ga), color(b, ba)


def main():
    ra = 0
    ba = 0
    ga = 0
    r = 0.5
    b = 0
    g = 1
    frame_delay_ms = 1000 // 30
    turtle.tracer(0)
    turtle.pensize(40)
    mouse_pos = add_mouse_listener()
    win = turtle.Screen()

    def tick():
        nonlocal ra, ba, ga
        turtle.color(colors(r, ra, g, ga, b, ba))
        ra += 0.03
        ba += 0.0311
        ga += 0.032
        x, y = mouse_pos()
        turtle.setheading(turtle.towards(x, y))
        turtle.forward(10)
        turtle.update()
        win.ontimer(tick, frame_delay_ms)

    tick()
    turtle.exitonclick()


if __name__ == "__main__":
    main()