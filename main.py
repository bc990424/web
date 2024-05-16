import turtle
from random import *
t=turtle.Turtle()
t.speed(0)

for i in range(200):
    t.pu()
    t.goto(randint(-800,800),randint(-800,800))
    t.begin_fill()
    t.color(random(),random(),random())
    si=randint(5,70)
    for x in range(5):
        t.fd(100)
        t.lt(144)
    t.end_fill()